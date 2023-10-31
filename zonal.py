#Zonal statistics for Rainfall

root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  if layer.name().startswith('3B-DAY'):
    prefix = layer.name()[-32:-26]
    params = {'INPUT_RASTER': layer.name(), 'RASTER_BAND': 1, 'INPUT_VECTOR': 'zmb_admbnda_adm2_2020', 'COLUMN_PREFIX': prefix+'_', 'STATS': 2}
    processing.run("qgis:zonalstatistics", params)
  