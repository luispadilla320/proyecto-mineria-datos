import streamlit as st
import pandas as pd
import plotly.express as px

# Config
st.set_page_config(
    page_title="Producto integrador",
    page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Escudo_UdeG.svg/1000px-Escudo_UdeG.svg.png",
    layout="wide"
    )

st.markdown(
    "<h1 style='text-align: center;'>Producto integrador. Proyecto final de minería de datos</h1>", 
    unsafe_allow_html=True
    )

hcol1, hcol2 = st.columns(2)
with hcol1:
    st.markdown("**Universidad de Guadalajara**")
    st.markdown("Análisis de información y minería de datos para la toma de decisiones")
    st.markdown("**Proyecto de minería de datos de un inventario de hardware de un data center**")
    st.markdown("Luis Eduardo Padilla Santoscoy")
    st.markdown("Código: 209382526")
with hcol2:
    hicol1, hicol2, hicol3 = st.columns(3)
    with hicol2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Escudo_UdeG.svg/1000px-Escudo_UdeG.svg.png", width=120)
    with hicol3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/68/Escudo_CUCEI.svg", width=120)
         

# Creamos pestañas
tab1, tab2, tab3= st.tabs(["**Definiciones sobre minería de datos**","**Vista minable**","**Dashboard de resultados**"])


with tab1:

    st.header("Definiciones")
    st.markdown("Temas y conceptos importantes en minería de datos.")

    icol1, icol2 = st.columns(2)

    # columna interna 1
    with icol1:
        st.markdown("**Sociedad de la información y del conocimiento**")
        st.markdown("""
        El concepto de sociedad de la información se refiere a la infraestructura técnica, enfocándose en la capacidad tecnológica para difundir datos a gran velocidad, mientras que la sociedad del conocimiento se refiere al paso en el que la habilidad para transformar esa información disponible en conocimiento útil para la sociedad se vuelve la prioridad.
        """)

        st.markdown("**Inteligencia de negocios BI y OLAP**")
        st.markdown("""
        * **Inteligencia de Negocios:** Se refiere al conjunto de técnicas enfocadas a la creación y administración de conocimiento sobre el medio, a partir del análisis de los datos existentes en una organización.
        * **OLAP abreviatura de on line analytical processing:** Es la tecnología que permite analizar datos desde varias perspectivas, ya que a diferencia de las bases de datos transaccionales, OLAP está diseñado para la consulta y el análisis al mismo tiempo, no para el mero registro.
        """)

        st.markdown("**Proceso de KDD y minería de los datos**")
        st.markdown("""
        **¿Qué es KDD?**
        KDD (*Knowledge Discovery in Databases*) es el proceso completo de extracción de conocimiento útil, válido, novedoso y comprensible a partir de grandes volúmenes de datos. La minería de datos es solo una etapa dentro de este proceso global.
        
        **Etapas del proceso KDD:**
        1.  **Selección:** Identificar y seleccionar el conjunto de datos objetivo.
        2.  **Preprocesamiento:** Limpieza de datos (tratar valores nulos, ruido, inconsistencias).
        3.  **Transformación:** Adecuar los datos al formato necesario (normalización, reducción de dimensiones).
        4.  **Minería de Datos (Data Mining):** Fase donde se aplican algoritmos inteligentes para extraer patrones.
        5.  **Interpretación/Evaluación:** Analizar si los patrones encontrados son válidos y útiles para el negocio.
        """)
        st.image("https://certificacionyequipos.altertechnology.com/wp-content/uploads/2024/02/Proceso-KDD.jpg", caption="Proceso del KDD")

    # columna interna 2
    with icol2:
        
        st.markdown("**Arquitectura de datos**")
        st.markdown("""
        * **ETL extract, transform y load:** Herramientas encargadas de mover datos desde múltiples fuentes a un almacén central. *Ejemplos:* Apache NiFi, Talend, Microsoft SSIS, Informatica PowerCenter.
        * **Data Warehouse (Almacén de Datos):** Base de datos corporativa que integra información depurada de toda la empresa para análisis histórico.
        * **Data Mart:** Un subconjunto del Data Warehouse enfocado en un área específica (ej. solo Ventas o solo Marketing).
        * **MOLAP (Multidimensional OLAP):** Almacenamiento de datos en cubos multidimensionales optimizados para velocidad.
        """)
        iacol1, iacol2, iacol3 = st.columns([0.5,2,0.5])
        with iacol2:
            st.image("https://www.channelbiz.es/wp-content/uploads/2015/07/ETL-Process.jpg", caption="ETL")

        
        st.markdown("**Técnicas y herramientas**")
        st.markdown("""
        * **Vista Minable:** Es la tabla final resultante del proceso de limpieza y transformación ETL, que por lo general se refiere a uns consulta SQL que creará una vista, dando origen al dataset listo para alimentar al algoritmo de minería.
        
        **Tareas y Técnicas:**
        Existen dos grandes tipos de tareas:
        1.  **Predictivas (Supervisadas):** Usan datos históricos para predecir el futuro.
            * *Técnicas:* Árboles de Decisión, Regresión, Redes Neuronales, SVM.
        2.  **Descriptivas (No Supervisadas):** Encuentran patrones ocultos o agrupaciones naturales.
            * *Técnicas:* Clustering (K-Means), Reglas de Asociación.
        
        **Herramientas de Minería:**
        * **Orange Data Mining:** Software de programación visual basado en componentes.
        * **Weka:** Colección de algoritmos de aprendizaje automático.
        * **RapidMiner:** Plataforma de ciencia de datos.
        """)
        iicol1, iicol2, iicol3 = st.columns([0.5,2,0.5])
        with iicol2:
            st.image("https://i.imgur.com/CtmxYrB.png",caption="Técnicas más usadas en minería")
with tab2:
    st.header("Almacén de datos y generacion de la vista minable")
    
    st.markdown("""
    Transformación de datos del SQL para poder generar una vista minable para alimentar el orange.
    """)

    st.subheader("Transformación ETL con SQL")
    st.markdown("Consulta utilizada para generar la vista minable:")

    st.code("""
    CREATE VIEW Vista_Minable_Falla_Costo AS
    SELECT
        -- seleccionando identificadores claves de la bd
        h.hardware_id,
        h.tipo_hardware,
        h.marca,
        h.modelo,
        h.estado, -- Columna a clasificar
        YEAR(CURDATE()) - YEAR(h.fecha_ingreso) AS Antiguedad_Anios, -- Feature calculado
        h.capacidad,

        -- sacando métricas del mantenimiento del hardware
        COUNT(m.mantenimiento_id) AS Total_Mantenimientos,
        SUM(m.costo) AS Costo_Total_Mantenimiento,
        MAX(m.fecha_mantenimiento) AS Ultimo_Mantenimiento_Fecha,
        SUM(CASE WHEN m.tipo_mantenimiento IN ('Sustitución RAM', 'Sustitución Disco Duro', 'Reemplazo Ventilador') THEN 1 ELSE 0 END) AS Total_Reemplazos_Mayor

    FROM
        hardware h
    LEFT JOIN
        mantenimiento m ON h.hardware_id = m.hardware_id
    GROUP BY
        h.hardware_id, h.tipo_hardware, h.marca, h.modelo, h.estado, Antiguedad_Anios, h.capacidad;

    """, language="sql")

    st.divider()

    st.subheader("Diccionario de variables")
    st.markdown("Definición de las columnas seleccionadas para la minería:")

    diccionario = {
        "Campo": ["hardware_id", "tipo, marca, modelo", "estado", "Antiguedad_Anios", "Total_Mantenimientos", "Costo_Total_Mantenimiento", "Total_Reemplazos_Mayor"],
        "Origen": ["Base de Datos", "Base de Datos", "Target (Objetivo)", "Calculado (SQL)", "Agregado (Count)", "Agregado (Sum)", "Agregado (Lógica)"],
        "Tipo": [
            "Identificador único.",
            "Variables categóricas para segmentar.",
            "Variable a predecir (Activo/Inactivo).",
            "Indicador de obsolescencia.",
            "Indica frecuencia de fallas.",
            "Mide el impacto del costo.",
            "Indica fallas críticas (Discos, RAM)."
        ]
    }
    st.table(pd.DataFrame(diccionario))

    st.divider()

    st.subheader("Vista minable final")
    st.markdown("Archivo csv generado con la estructura para la minería de los datos.")

    try:
        
        df_final_vista = pd.read_csv("vista_minable.csv")
        
        st.dataframe(df_final_vista, use_container_width=True)
        
        csv_export = df_final_vista.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar archivo (.csv)",
            data=csv_export,
            file_name="vista_minable.csv",
            mime="text/csv"
        )
        st.success(f"Archivo cargado: {len(df_final_vista)} registros.")

    except FileNotFoundError:
        st.warning("No encuentro el archivo 'vista_minable.csv'.")
        st.info("Sube tu archivo CSV con ese nombre a la carpeta del proyecto.")
with tab3:
    st.header("Análisis de resultados de predicción")
    
    try:
        # Carga del archivo
        df = pd.read_csv("resultados.csv", skiprows=[1, 2])
        
        # Métricas 
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Equipos", len(df))
        if 'estado' in df.columns:
            col2.metric("Equipos Activos", len(df[df['estado'] == 'Activo']))
            col3.metric("Equipos Inactivos", len(df[df['estado'] == 'Inactivo']), delta_color="inverse")
        
        st.divider()

        st.subheader("Selección de modelo")
        
        #with st.expander("Explicación de la matriz"):
        st.markdown("""
        Esta tabla se compara la realidad de los datos contra la predicción realizada, donde en la diagonal son los aciertos del modelo mientras que fuera son los errores, buscando el objetivo es detectar los equipos inactivos que representan las fallas. De manera que los porcentajes muestran las comparaciones de ambos modelos de árbol y bosque.
        """)

        col_conf1, col_conf2 = st.columns(2)
        
        with col_conf1:
            st.markdown("##### Configuración")
            
            # 1. FIJAMOS la columna Real
            col_real = 'estado'
            
            # 2. Filtramos columnas para dejar SOLO los modelos en el menú
            cols_datos = ['estado', 'marca', 'tipo_hardware', 'modelo', 'Antiguedad_Anios', 'capacidad', 'Total_Mantenimientos', 'Costo_Total_Mantenimiento', 'Total_Reemplazos_Mayor']
            posibles_modelos = [c for c in df.columns if c not in cols_datos and df[c].dtype == 'object']
            
            # Seguridad por si no encuentra modelos
            if not posibles_modelos: 
                posibles_modelos = [c for c in df.columns if c != col_real]

            col_pred = st.selectbox("Selecciona el Modelo a Evaluar:", posibles_modelos)

        with col_conf2:
            if col_real in df.columns and col_pred:
               
                matriz = pd.crosstab(df[col_real], df[col_pred])
                st.write(f"**Matriz: Realidad vs {col_pred}**")
                
                st.dataframe(matriz.style.background_gradient(cmap='Greens'))
                
                aciertos = df[df[col_real] == df[col_pred]].shape[0]
                accuracy = (aciertos / len(df)) * 100
                st.metric(label=f"Precisión Global", value=f"{accuracy:.1f}%")
            else:
                st.error(f"No encuentro la columna '{col_real}' en el CSV.")

 
        #### Predicciones
        st.divider()

        st.subheader("Tabla de predicciones de fallos")
        st.markdown("""
        **Explicación de tabla:**
        * El riesgo de que un elemento se vaya a reparación aparece en la barra, que representa la probabilidad matemática de que el equipo pase a estado inactivo.
        * Cuando aparece en 0.00 el modelo asegura de que el equipo está activo.
        * Mientras que cuando sale 1.00 el modelo asegura que el equipo va a fallar.
        * Los valores intermedios muestran un porcentaje de cierto riesgo.
        """)
        
        col_f1, col_f2, col_f3 = st.columns(3)
        
        with col_f1:
            opciones_marca = df['marca'].unique() if 'marca' in df.columns else []
            marca_sel = st.multiselect("Filtrar por Marca:", opciones_marca)

        with col_f2:
            opciones_tipo = df['tipo_hardware'].unique() if 'tipo_hardware' in df.columns else []
            tipo_sel = st.multiselect("Filtrar por Tipo:", opciones_tipo)
            
        with col_f3:
            ver_riesgos = st.checkbox("Ver solo equipos con Riesgo (> 0%)", value=True)

        df_view = df.copy()
        
        #aplicacion de filtros
        if marca_sel:
            df_view = df_view[df_view['marca'].isin(marca_sel)]
        if tipo_sel:
            df_view = df_view[df_view['tipo_hardware'].isin(tipo_sel)]

        col_prob_inactivo = f"{col_pred} (Inactivo)"

        if col_prob_inactivo in df_view.columns:
            
            # Filtro de riesgos
            if ver_riesgos:
                df_view = df_view[df_view[col_prob_inactivo] > 0]

            cols_deseadas = ['modelo', 'tipo_hardware', 'marca', col_real, col_pred, col_prob_inactivo]
            
            cols_finales = [c for c in cols_deseadas if c in df_view.columns]
            df_final = df_view[cols_finales]

            # Visualizacion 
            st.dataframe(
                df_final,
                column_config={
                    col_prob_inactivo: st.column_config.ProgressColumn(
                        "Riesgo de Falla", 
                        help="Probabilidad de pasar a Inactivo (0=Sano, 1=Falla)",
                        format="%.2f",
                        min_value=0,
                        max_value=1,
                    ),
                    col_real: st.column_config.TextColumn("Estado real"),
                    col_pred: st.column_config.TextColumn("Predicción"),
                    'tipo_hardware': st.column_config.TextColumn("Tipo"),
                },
                hide_index=True,
                use_container_width=True
            )
            
        else:
            st.warning(f"No encontré la columna de probabilidades '{col_prob_inactivo}'.")
            st.dataframe(df_view)

    except Exception as e:
        st.error(f"Error en el explorador: {e}")

        st.divider()

#with tab4:

    st.header("Segmentación de equipos con agrupamientos de clustering")
    
    st.markdown("""
    **Objetivo:** Agrupar los dispositivos en categorías automáticas basadas en sus similitudes 
    (costo, antigüedad, capacidad) para descubrir patrones ocultos.
    """)
    
    st.markdown("""
    El k-means es un algoritmo no supervisado que a diferencia de la predicción, aquí no le decie al sistema qué cosa buscar, sino que el algoritmo agrupa los datos buscando tendencias matemáticas haciendo clusters.
    """)

    try:
        df_cluster = pd.read_csv("clusters.csv", skiprows=[1, 2])
        
        if 'Silhouette' in df_cluster.columns:
            promedio_sil = df_cluster['Silhouette'].mean()
            
            col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
            col_kpi1.metric("Total de Equipos", len(df_cluster))
            col_kpi2.metric("Clusters Identificados", df_cluster['Cluster'].nunique())
            
            st.markdown("Prueba de separación de grupos para el clustering:")
            col_kpi3.metric("Calidad (Silhouette)", f"{promedio_sil:.3f}")
            if promedio_sil > 0.5:
                st.success("Separación clara de clusters.")
            elif promedio_sil > 0.25:
                st.info("Tendencias poco claras")
            else:
                st.warning("No se identifican tendencias.")
        
        st.divider()


        st.subheader("Mapa de clusters")
        st.markdown("""**Explicación de resultados del mapa:**""")
        st.markdown("🔴 Cluster 1 de riesgo alto: Son equipos con alto costo de mantenimiento y también con mucho tiempo de antigüedad, por lo tanto son candidatos a reemplazo inmediato.")
        st.markdown("🟢 Cluster 2 de estables: Aquí hay equipos con bajo costo con poca antigüedad y pocos mantenimientos.")
        st.markdown("🔵 Cluster 3 de equipos con anomalías por fallas prematuras: Salen equipos de poca antigüedad pero con muchos mantenimientos y costosos, que se asume que eequieren revisión.")
        

        col_c1, col_c2 = st.columns([1, 3])
        
        with col_c1:
            st.markdown("##### ⚙️ Ejes")
            
            opciones_clave = ['Antiguedad_Anios', 'Costo_Total_Mantenimiento', 'Total_Mantenimientos']
            
            
            ejes_disponibles = [c for c in opciones_clave if c in df_cluster.columns]
            
            x_axis = st.selectbox("Eje X:", ejes_disponibles, index=0) # Por defecto: Antiguedad
            y_axis = st.selectbox("Eje Y:", ejes_disponibles, index=1 if len(ejes_disponibles)>1 else 0) # Por defecto: Costo
            
            filtro_tipo = st.multiselect("Filtrar por Tipo:", df_cluster['tipo_hardware'].unique())

        with col_c2:
            
            data_to_plot = df_cluster.copy()
            if filtro_tipo:
                data_to_plot = data_to_plot[data_to_plot['tipo_hardware'].isin(filtro_tipo)]
            
            if x_axis and y_axis:
                fig = px.scatter(
                    data_to_plot,
                    x=x_axis,
                    y=y_axis,
                    color='Cluster',          
                    size='Silhouette',        
                    
                    
                    hover_data=['tipo_hardware', 'marca', 'modelo', 'estado'], 
                    
                    title=f"Distribución: {x_axis} vs {y_axis}",
                    color_discrete_sequence=px.colors.qualitative.Set1 # Colores bonitos y distintos
                )
                
               
                fig.update_layout(xaxis_title=x_axis, yaxis_title=y_axis)
                
               
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No se encontraron las columnas necesarias para graficar.")

        st.divider()
        

    except FileNotFoundError:
        st.error("No encuentro el archivo 'clusters.csv'. Recuerda exportarlo desde Orange.")
    except Exception as e:
        st.error(f"Error cargando datos: {e}")




