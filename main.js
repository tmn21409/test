(function() {
  "use strict";

var viewer = new Cesium.Viewer("cesium");

viewer.dataSources.add(Cesium.KmlDataSource.load("./01_L1_case01.kmz"));

	//�����̎��_�i�J�����j�̈ʒu ���{�̏��ɃJ����������悤�ɐݒ�B
  viewer.camera.setView({
   destination: Cesium.Cartesian3.fromDegrees(138, 29, 4000000),
   orientation: {
     heading: 0, // ���������̉�]�x�i���W�A���j
     pitch: -1.4, // ���������̉�]�x�i���W�A���j ������グ���艺�������낵����
     roll: 0
  }
});

}());