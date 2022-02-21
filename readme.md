## data_vizzes readme

Repo con distintas visualizaciones  

### genero_calles
Mapa interactivo que muestra las calles con nombres de mujeres y nombres de hombres.
Las calles se bajan de OSM. Las calles que no son nombres se agrupan en qgis para que sea un solo feature.
Dado que son demasiadas features, se usó qgis para reducir los pesos de males y not_named usando geoprocesos de simplify & collect geometries. Los archivos geojson se reducen según lo siguiente:  

- male 11mb
- simp 9.2
- coll  2.8
- coll_all simp10 1.3


- not_named 76.8
- select vars 35mb
- select coll 18.6
- select coll_all simp10 11.2

Refe para paleta: https://blog.datawrapper.de/gendercolor/

### genero_gabinete
Contiene la visualización del género del primer gabinete de Pedro Castillo en comparación con la de los x últimos.