//.setStartX(126.5).setStartY(35.2) <= ����� �ɼ�
    public void onClick(View v) {
        if(v.getId() == R.id.button){
            Location destination = Location.newBuilder("īī�� �Ǳ� ���ǽ�", 127.10821222694533, 37.40205604363057).build();
            List<Location> waypoint = new ArrayList<Location>();
            waypoint.add(Location.newBuilder("������", 126.8322289016308, 37.528495607451205).build());
            KakaoNaviParams params;
            NaviOptions options = NaviOptions.newBuilder().setCoordType(CoordType.WGS84).setVehicleType(VehicleType.FIRST).setRpOption(RpOption.SHORTEST).build();
            if(waypoint.size()>0) {
                KakaoNaviParams.Builder builder = KakaoNaviParams.newBuilder(destination).setNaviOptions(options).setViaList(waypoint);
                params = builder.build();
            }else {
                KakaoNaviParams.Builder builder = KakaoNaviParams.newBuilder(destination).setNaviOptions(options);
                params = builder.build();
            }
            KakaoNaviService.getInstance().navigate(MainActivity.this, params);
        }
    }