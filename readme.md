## genero_calles readme

Mapa interactivo que muestra las calles con nombres de mujeres en Lima y Callao.
Las calles se bajan de OSM.
Las calles que no son nombres se agrupan en qgis para que sea un solo feature.
Dado que son demasiadas features, se usó qgis para reducir los pesos de males y not_named usando geoprocesos de collect geometries y simplify (tolerance = 10)

El mapa se encuentra aquí

Se publicó un hilo de twitter aquí