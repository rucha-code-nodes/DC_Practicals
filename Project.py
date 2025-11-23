

import numpy as np            
from sklearn.linear_model import LinearRegression

hours = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1,1)
marks = np.array([20,25,30,35,40,50,60,65,80])  


model = LinearRegression()
model.fit(hours, marks)


h = float(input("Enter hours studied: "))


predicted_marks = model.predict([[h]])[0]

if predicted_marks >= 40:
    print("Marks =", predicted_marks, "→ 🎉 Student will PASS")
else:
    print("Marks =", predicted_marks, "→ ❌ Student will FAIL")
