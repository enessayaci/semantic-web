from flask import Flask, render_template, request
import myQuery as myQuery
import requirements_generator
r=requirements_generator.scan(".")
r.save()
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('search.html',list =[]) #uygulama çalıştığında bu sayfayı açıyorum
@app.route('/', methods=['POST'])
def get_value():

    searchInput=request.form['search']  #arama motorundan girdi alıyorum
    listOfExperimentsOfPopPerson = []
    if len(searchInput) == 0: # eğer girdi boş ise aynı sayfaya tekrar yönlendiriyorum
        return render_template('search.html',list=[],alert="input cant be empty!")  # aynı sayfaya yönlendiriyorum
    else:
        queryResult = myQuery.search(searchInput)


        if len(queryResult)>0:
            popPerson = queryResult[0]
        else:
            infoMessage = "There is no person on database who has studied on the subject "
            return render_template('search.html', list=[], key=searchInput,infoMessage=infoMessage, infoMessage2=" ")

        listOfExperimentsOfPopPerson = [{"companyName":popPerson[0]}]
        for i in popPerson[1]:
            element = {"companyName":i}
            listOfExperimentsOfPopPerson.append(element)


        infoMessage ="Companies graph has been drawn for the most related person on database who has studied on the subject "
        infoMessage2="hover on circles to see company names"
        return render_template('search.html', list = listOfExperimentsOfPopPerson,key=searchInput,infoMessage=infoMessage,infoMessage2=infoMessage2)

if __name__ == '__main__':
    app.run(debug=True)