from flask import Flask

app = Flask(__name__)

@app.route('/food1')
def food1():
    return("""<html> <h2> food </h2> <img src='https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/6/12/3/FNM070116_Penne-with-Vodka-Sauce-and-Mini-Meatballs-recipe_s4x3.jpg.rend.hgtvcom.1280.1280.suffix/1465939620872.jpeg' width = '400' hight = '400'> 
       <br> <a href = '/home'> return to home <br> <a href= '/food2'> go to another photo </html>""")

@app.route('/home')
def home():
    return("""<html> <h1>gallery</h1> <p> photo gallery containing three types of photos: food, pets, and outer space.</p>  
            <a href = '/food1'> go to the first food photo <br> <a href = '/pet2'> go to the second pet photo <br> <a href = '/space1'> go to the space photo </html>""")
    
@app.route('/food2')
def food2():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLQzQqVBk7LmMbMSaEuRy3AkVv1lyGqThm4Q&s' width = '400' hight = '400'> 
       <br> <a href = '/food1'> return <br> <a href= '/food3'> go to another photo </html> """)

@app.route('/food3')
def food3():
    return(""" <html> <img src='https://nypost.com/wp-content/uploads/sites/2/2024/03/unhealthy-products-food-bad-figure-78246698.jpg?quality=75&strip=all&w=1024' width = '400' hight = '400'> 
       <br> <a href = '/home'> return to home<br> <a href= '/food2'> return </html> """)

@app.route('/pet2')
def pet2():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwuhnCOZ9tbBPL1z6Rchv62bb02PmC6mPvYQ&s' width = '400' hight = '400'> 
       <br> <a href = '/pet1'> go to pet1 <br> <a href= '/pet3'> go to pet3 <br> <a  href = '/home'> go to home </html> """)

@app.route('/pet1')
def pet1():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbetk5kG1hDJev0_0VcBgdJ_1kt2lso_GgJQ&s' width = '400' hight = '400'> 
       <br> <a href = '/pet2'> go to pet2 </html> """)

@app.route('/pet3')
def pet3():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYFUy7E0CDruPtRlAh_BYERn46N6NpOD_zvg&s' width = '400' hight = '400'> 
       <br> <a href = '/pet2'> go to pet2 </html> """)

@app.route('/space1')
def space1():
    return(""" <html> <img src='https://prd-sc102-cdn.rtx.com/-/media/ca/product-assets/marketing/s/space/space-symposium-graphic_1920x1080.jpg?rev=2a22f490c9c644a5bf69ef3cce59813d' width = '400' hight = '400'> 
       <br> <a href = '/space2'> go to space2 <br> <a href = '/space3'> go to space3 <br> <a href = '/home'> go to home </html> """)


@app.route('/space2')
def space2():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s' width = '400' hight = '400'> 
       <br> <a href = '/space1'> go to space1 <br> <a href = '/space3'> go to space3 </html> """)

@app.route('/space3')
def space3():
    return(""" <html> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSva80qn921XF6JDyEMAvAcAibZTDL4nIuOdA&s' width = '400' hight = '400'> 
       <br> <a href = '/space1'> go to space1 <br> <a href = '/space2'> go to space2 </html> """)



if __name__ == '__main__':
    app.run(debug=True)