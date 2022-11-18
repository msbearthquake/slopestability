import   streamlit  as st; from PIL import Image; import numpy  as np
from  sklearn.ensemble   import   RandomForestRegressor
import pandas  as pd; import pickle

import os


filename1 = 'https://github.com/msbearthquake/slopestability-/blob/main/Capture1.PNG'
filename2 = 'https://github.com/msbearthquake/slopestability-/blob/main/Capture2.PNG'

st.title('Slope stability prediction under seismic conditions')
with st.container():

    st.image(filename1)
    st.image(filename2)

SHV = st.number_input('Insert Slope height:',0.0)
AIV = st.number_input('Insert angle of inclination:',0.0)
CV = st.number_input('Insert cohesion:',0.0)
FAV = st.number_input('Insert friction angle:',0.0)
PGAV = st.number_input('Insert peak ground acceleration:',0.0)
inputvec = np.array([SHV, AIV, CV, FAV, PGAV])


filename3 = 'finalized_model.sav'
### save the model to disk
# pickle.dump(model, open(filename, 'wb'))
 
### some time later...
### load the model from disk


with st.container():

    if st.button('Run'):
        if SHV!=0 and CV>15:
            loaded_model = pickle.load(open(filename3, 'rb'))

            yhat1 = loaded_model.predict(inputvec.reshape(1,-1))
            if  yhat1[0] == 0:
                resu = "False"   
            else:
                resu = "True"   

            st.write("Is slope stable? " , resu, "m")
        elif (SHV==0):
            st.write("Slope height should not be zero.")
        elif(AIV<15 or CV<15 or FAV<15):
            st.write("Angle of inclination, cohesion, and friction angle should be > 15.")



# st.write(trainx)

filename3 = 'https://github.com/msbearthquake/slopestability-/blob/main/Capture3.PNG'


with st.container():
    st.header("Developer:")

    st.image(filename3)
 



