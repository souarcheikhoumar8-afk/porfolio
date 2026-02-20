import streamlit as st 
# 1. CONFIGURATION DE LA PAGE (Doit être la première commande)
st.set_page_config(page_title="Mon Portfolio", page_icon="👤", layout="wide") 

# 2. BARRE LATÉRALE : PHOTO ET CONTACT
with st.sidebar:
    st.info("Informations Personnelles")
    st.write("📍 Adresse : Kedougou, senegal")
    st.write("📞 Téléphone : +221785992520")
    st.write("📧 Email : souarcheikhoumar8@gmail.com.")
    
# 3. CONTENU PRINCIPAL 
st.title("Portfolio Professionnel")
# Section Éducation et Expériences (en 2 colonnes) 
col1, col2 = st.columns(2)

with col1: 
    st.header("🎓Education")
    st.markdown(""")
                st.licence,(en gestion du patrimoine_Universite Gaston berger de Saint-Louis)
                st.Saiminaire,(de formation en gestion relation et technique de vent-(BCC),DAKAR)
                st. Baccalauréat,(Lycée Alpha molo Balde (2018))
                
with col2:
st.header("💼Expérience")
st.markdown(""")
    st.write(" Au Musée Théodore Monod d'Art Africain ")
    st.write("commerciale-NSIA ASSURANCE VIE,Dakar")

    st.write("---")

    # section Competences
    st.header("competence")
    skills_col1, skills_col2, skills_col3 =st.columns(3)
    with skills_col1:
        st.subheader("Techniques")
        st.write("collecte de donnees sur les terrain,traitement des donnees")
        st.write("une maitrise des logiciels Bureautique")
        st.write("programmation avec python et steamlit")
        st.write("creation de cartes thematique et situation")
    with skills_col2:
        st.subheader("outils")
        st.write("Arcmap, QGIS")
        st.write("word,excel,power point,googledog")
                 
                 
    
    
     

               
    
              
    
               
     
                
      