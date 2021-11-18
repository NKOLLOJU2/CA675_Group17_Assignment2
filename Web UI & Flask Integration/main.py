from flask import Flask, render_template,request
import mysql.connector

app=Flask(__name__)

connection = mysql.connector.connect(user='root', password='root', host='34.105.141.184', database='BookStore')
cursor = connection.cursor()
Query1 = ("select A.author_id,author_name from Author A , (select author_id,count(book_id) book_count from Book_Author group by author_id having count(book_id)>50) BA where A.author_id=BA.author_id")
Query2 = ("select category_id,category_name from Categories")
Query3 = ("select format_id,format_name from Formats")
cursor.execute(Query1)
joblist1=cursor.fetchall()
cursor.execute(Query2)
joblist2 = cursor.fetchall()
cursor.execute(Query3)
joblist3 = cursor.fetchall()

@app.route('/')
def home():
    return render_template('index.html',joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)



@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        value=request.form['Source']
        print(value)
        Query2=("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,group_concat(C.category_name) as Genres,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where BA.author_id={value} group by B.title,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url;".format(value=value))
        cursor.execute(Query2)
        info=cursor.fetchall()
        print(info)
    return render_template('search.html',info=info,joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)


@app.route('/search_categories',methods=['GET','POST'])
def search_categories():
    if request.method=='POST':
        value=request.form['Source']
        print(value)
        Query=("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where C.category_id={value}".format(value=value))
        cursor.execute(Query)
        info=cursor.fetchall()
        print(info)
    return render_template('search_categories.html',info=info,joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)


@app.route('/search_ratings',methods=['GET','POST'])
def search_ratings():
    if request.method=='POST':
        value=request.form['Source']
        if value==1:
            Query=("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where B.rating_avg between 0 and 1 limit 100")
        elif value==2:
            Query = ("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where B.rating_avg between 1 and 2 limit 100")
        elif value==3:
            Query = ("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where B.rating_avg between 2 and 3 limit 100")
        elif value==4:
            Query = ("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where B.rating_avg between 3 and 4 limit 100")
        else:
            Query = ("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where B.rating_avg between 4 and 5 limit 100")
        cursor.execute(Query)
        info=cursor.fetchall()
        print(info)
    return render_template('search_categories.html',info=info,joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)


@app.route('/search_format',methods=['GET','POST'])
def search_format():
    if request.method=='POST':
        value=request.form['Source']
        #Query=("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,group_concat(C.category_name) as Genres,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where F.format_id={value} group by B.title,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url limit 100".format(value=value))
        Query = ("SELECT B.title as BookTitle,A.author_name,B.bestsellers_rank ,B.lang,B.rating_avg,F.format_name,B.url FROM Books B inner join Book_Author BA on B.book_id=BA.book_id inner join Book_Category BC on B.Book_id=BC.book_id inner join Formats F on B.format_id=F.format_id inner join Categories C on BC.category_id=C.category_id inner join Author A on A.author_id=BA.author_id where F.format_id={value} limit 100".format(value=value))
        cursor.execute(Query)
        info=cursor.fetchall()
        print(info)
    return render_template('search_format.html',info=info,joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)

@app.route('/search_analytics1',methods=['GET','POST'])
def search_analytics1():
    if request.method == 'POST':
        value = request.form['Source']
        print(value)
        if value == "1":
            return render_template('search_analytics.html',joblist1=joblist1,joblist2=joblist2,joblist3=joblist3)
        if value == "2":
            return render_template('search_analytics1.html', joblist1=joblist1, joblist2=joblist2, joblist3=joblist3)
        if value == "3":
            return render_template('search_analytics2.html', joblist1=joblist1, joblist2=joblist2, joblist3=joblist3)
        if value == "4":
            return render_template('search_analyics3.html', joblist1=joblist1, joblist2=joblist2, joblist3=joblist3)
        if value == "5":
            return render_template('search_analytics4.html', joblist1=joblist1, joblist2=joblist2, joblist3=joblist3)


if __name__=='__main__':
    app.run(debug=True)