## genero_calles readme

Mapa interactivo que muestra las calles con nombres de mujeres en Lima y Callao.

El mapa interactivo se encuentra [aquí](https://desarroio.github.io/genero-calles/)

Se publicó un hilo de twitter [aquí](https://twitter.com/desarro_io/status/1501264092203388937)

La clasificación fue realizada detectando la presencia de nombres populares de hombres y mujeres en la información pública disponible en Open Street Map, y realizando ajustes manuales sobre esos resultados. Algunas calles pueden haber sido clasificadas como "sin nombres de personas" debido a errores u omisiones involuntarias en este método o a errores ortográficos en los datos iniciales.

Las calles que no son nombres se agrupan en Qgis para que sea un solo feature. Dado que son demasiadas features, se usó qgis para reducir los pesos de males y not_named usando geoprocesos de collect geometries y simplify (tolerance = 10).

Los nombres de calles son de [OpenStreetMap](https://www.openstreetmap.org/) 🔎, el mapa se hizo con [Leaflet](https://leafletjs.com/) 🍃 y tiles 🗺️ de [Carto](https://carto.com/)

Nuestro código es de libre acceso bajo una licencia MIT.