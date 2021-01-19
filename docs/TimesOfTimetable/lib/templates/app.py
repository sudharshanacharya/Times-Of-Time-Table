from flask import Flask, request, render_template

@app.route("/add_persons_button", methods=['POST'])
def add_persons_button():
    Pid = request.form.get('Pid')
    Name = request.form.get('Name')
    Age = request.form.get('Age')
    City = request.form.get('City')
    District = request.form.get('District')
    State = request.form.get('State')
    Snake_type = request.form.get('Snake_type')
    Snake_colour = request.form.get('Snake_colour')

    cursor.execute("""
                INSERT INTO Person(Pid,Name,Age,City,District,State,Snake_type,Snake_colour) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """, (Pid, Name, Age, City, District, State, Snake_type, Snake_colour))
    mydb.commit()
    return redirect(url_for('view_av_centres'))


@app.route("/view_av_centres")
def view_av_centres():
    cursor.execute(
        """SELECT DISTINCT(A.Facility_ID),A.Facility_Name,A.City,A.District,A.State,A.Contact_no,A.AV_Name,A.Available_Qty,A.AV_Price FROM AV_Centre A,PERSON P  WHERE P.STATE=A.STATE """)
    antivenom_query = cursor.fetchall()
    return render_template("av_details.html", av=antivenom_query)