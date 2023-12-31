
from acceuilview import acceuil
from objectifs import objectifs
from personnalisation import personnalisation
from guide import guide
from exploration import exploration
from predictionview import get_feature_and_predict
import streamlit as st 
import matplotlib.pyplot as plt 
import pandas as pd 

frame = 0

def main(): 
    # Logo
    logo_menu = "../assets/logo_menu.png"
    st.sidebar.image(logo_menu, use_column_width=False, width=300)

    page_bg_img = """
    <style> [data-testid="stSidebar"] {
        background: linear-gradient(90deg, #5675a3, rgba(161,195,221,1))
    </style> 
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
     # Barre latérale
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            position: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Barre latérale
    #st.sidebar.title("PowerForecast")
    #st.sidebar.subheader("Dashbord")
    
    #Mise en place des box de selections
   # selectbox = st.sidebar.selectbox("A propos", ["Acceuil", "Objectifs", ""]) #A propos du projet
    selectbox2 = st.sidebar.selectbox("Actions", ["Acceuil", "Objectifs","Analyse exploratoire", "Personnalisation", "Prediction","Guide"]) #Action de l'utilisateur

    #appel de la page acceuil
    if selectbox2 == "Acceuil":
        #st.experimental_rerun()
        #Exploration des données
        acceuil() 
        
    elif selectbox2 == "Objectifs":
        #st.experimental_rerun()
        #Exploration des données
        objectifs()
        
    if selectbox2 == "Analyse exploratoire":
        #st.experimental_rerun()
        #Exploration des données
        exploration()
        
        #Ecran de personnalisation
    elif selectbox2 == "Personnalisation":
        #st.experimental_rerun()
        personnalisation()
        
        #Appell de l'interface de prediction
    elif selectbox2 == "Prediction":
        #st.experimental_rerun()
        get_feature_and_predict()
        
    elif selectbox2 == "Guide":
        #st.experimental_rerun()
        guide()
    
        
        
    
    # Utilisez les valeurs des widgets dans le contenu principal
    st.write("A propos sélectionnée :", selectbox2)
    
    

if __name__ == "__main__":
    main()