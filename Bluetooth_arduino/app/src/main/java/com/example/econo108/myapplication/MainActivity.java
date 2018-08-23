package com.example.econo108.myapplication;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v4.app.ActivityCompat;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.Manifest;

public class MainActivity extends Activity implements OnClickListener {
    // Debugging
    private static final String TAG = "Main";

    // Intent request code
    private static final int REQUEST_CONNECT_DEVICE = 1;
    private static final int REQUEST_ENABLE_BT = 2;

    // Layout
    private Button btn_Connect;
    private TextView txt_Result;

    private BluetoothService btService = null;


    private final Handler mHandler = new Handler() {

        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);

            Bundle bundle = msg.getData();
            final String available = bundle.getString("available");
            final String velocity = bundle.getString("velocity");
            updateThreadTextView(available, velocity);
        }

    };

    private void updateThreadTextView(String available, String velocity){
      txt_Result.setText("Available : " + available + " / Velocity : " + velocity);
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.e(TAG, "onCreate");
        int MY_PERMISSIONS_REQUEST_ACCESS_COARSE_LOCATION = 1;

        ActivityCompat.requestPermissions(this,

                new String[]{Manifest.permission.ACCESS_COARSE_LOCATION},

                MY_PERMISSIONS_REQUEST_ACCESS_COARSE_LOCATION);

        setContentView(R.layout.activity_main);

        /** Main Layout **/
        btn_Connect = (Button) findViewById(R.id.btn_connect);
        txt_Result = (TextView) findViewById(R.id.txt_result);

        btn_Connect.setOnClickListener(this);

        // BluetoothService Ŭ���� ����
        if(btService == null) {
            btService = new BluetoothService(this, mHandler);
        }
    }

    @Override
    public void onClick(View v) {
        if(btService.getDeviceState()) {
            // ��������� ���� ������ ����� ��
            btService.enableBluetooth();
        } else {
            finish();
        }
    }

    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        Log.d(TAG, "onActivityResult " + resultCode);

        switch (requestCode) {

            case REQUEST_CONNECT_DEVICE:
                // When the request to enable Bluetooth returns
                if (resultCode == Activity.RESULT_OK) {
                    btService.getDeviceInfo(data);
                }
                break;
            case REQUEST_ENABLE_BT:
            // When the request to enable Bluetooth returns
                if (resultCode == Activity.RESULT_OK) {
                    // Next Step
                    btService.scanDevice();
                } else {

                    Log.d(TAG, "Bluetooth is not enabled");
                }
                break;
        }
    }
}
