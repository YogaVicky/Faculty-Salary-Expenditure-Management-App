from flask import Flask, render_template, request
import os
from datetime import datetime
#from werkzeug import secure_filename
from pymysql import connect

app = Flask(__name__)

def dbconnect(sql):
    result = []
    db = connect(host='remotemysql.com', database='xl8iiwrc7M', user='xl8iiwrc7M', password='SxRw9vgpPS')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    for i in cursor.fetchall():
        result.append(i)
    cursor.close()
    return result

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('form.html')

@app.route('/faculty',methods = ['POST', 'GET'])
def faculty():
    if request.method == 'POST':
        res = request.form
        print(res)
        eid = int(res['id'])
        ename = res['name']
        quarters = int(res['quarters'])
        bp = int(res['basic'])
        
        tot = []
        for i in range(0,24):
            tot.append(0)
        
        g18=0
        g20=0
        bp1 = 1.03*bp
        bp2 = 1.03*bp1
        sql = "insert into basicpay(eid, ename, april18bp, may18bp, june18bp, july18bp, august18bp, september18bp, october18bp, november18bp, december18bp, january19bp, february19bp, march19bp, april19bp, may19bp, june19bp, july19bp, august19bp, september19bp, october19bp, november19bp, december19bp, january20bp, february20bp, march20bp, quarters) VALUES ({0},'{1}',{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26})".format(eid,ename,bp,bp,bp,bp,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp1,bp2,bp2,bp2,bp2,bp2,bp2,bp2,bp2,quarters)
        print(sql)
        res = dbconnect(sql)
        
        tot[0]+=bp
        tot[1]+=bp
        tot[2]+=bp
        tot[3]+=bp
        tot[4]+=bp1
        tot[5]+=bp1
        tot[6]+=bp1
        tot[7]+=bp1
        tot[8]+=bp1
        tot[9]+=bp1
        tot[10]+=bp1
        tot[11]+=bp1
        tot[12]+=bp1
        tot[13]+=bp1
        tot[14]+=bp1
        tot[15]+=bp1
        tot[16]+=bp2
        tot[17]+=bp2
        tot[18]+=bp2
        tot[19]+=bp2
        tot[20]+=bp2
        tot[21]+=bp2
        tot[22]+=bp2
        tot[23]+=bp2

        g18+=4*bp + 8*bp1
        g20+=4*bp1 + 8*bp2

        if quarters != 0:
            hra = int(0.24*bp)
            hra1 = int(0.24*bp1)
            hra2 = int(0.24*bp2)
        else:
            hra = 0
            hra1=0
            hra2=0

        tot[0]+=hra
        tot[1]+=hra
        tot[2]+=hra
        tot[3]+=hra
        tot[4]+=hra1
        tot[5]+=hra1
        tot[6]+=hra1
        tot[7]+=hra1
        tot[8]+=hra1
        tot[9]+=hra1
        tot[10]+=hra1
        tot[11]+=hra1
        tot[12]+=hra1
        tot[13]+=hra1
        tot[14]+=hra1
        tot[15]+=hra1
        tot[16]+=hra2
        tot[17]+=hra2
        tot[18]+=hra2
        tot[19]+=hra2
        tot[20]+=hra2
        tot[21]+=hra2
        tot[22]+=hra2
        tot[23]+=hra2

        g18+=4*hra+8*hra1
        g20+=4*hra1+8*hra2 
        sql = "insert into hra(eid,april18hra, may18hra, june18hra, july18hra, august18hra, september18hra, october18hra, november18hra, december18hra, january19hra, february19hra, march19hra, april19hra, may19hra, june19hra, july19hra, august19hra, september19hra, october19hra, november19hra, december19hra, january20hra, february20hra, march20hra) VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24})".format(eid,hra,hra,hra,hra,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra1,hra2,hra2,hra2,hra2,hra2,hra2,hra2,hra2)
        print(sql)
        res = dbconnect(sql)

        lfee = 0
        if quarters == 1:
            lfee = 150
        elif quarters == 2:
            lfee = 310
        elif quarters == 3:
            lfee = 470
        elif quarters == 4:
            lfee = 680
        elif quarters == 5:
            lfee = 1270
        else:
            lfee = 1870

        tot[0]-=lfee
        tot[1]-=lfee
        tot[2]-=lfee
        tot[3]-=lfee
        tot[4]-=lfee
        tot[5]-=lfee
        tot[6]-=lfee
        tot[7]-=lfee
        tot[8]-=lfee
        tot[9]-=lfee
        tot[10]-=lfee
        tot[11]-=lfee
        tot[12]-=lfee
        tot[13]-=lfee
        tot[14]-=lfee
        tot[15]-=lfee
        tot[16]-=lfee
        tot[17]-=lfee
        tot[18]-=lfee
        tot[19]-=lfee
        tot[20]-=lfee
        tot[21]-=lfee
        tot[22]-=lfee
        tot[23]-=lfee
        
        sql = "insert into quarters(eid,licencefee) values({0},{1})".format(eid,lfee)
        print(sql)
        res = dbconnect(sql)

        if bp >= 100000:
            ta = 8000
        else:
            ta = 5000
        
        if bp1 >= 100000:
            ta1 = 8000
        else:
            ta1 = 5000

        if bp2 >= 100000:
            ta2 = 8000
        else:
            ta2 = 5000
        
        sql = "insert into ta(eid,april18ta, may18ta, june18ta, july18ta, august18ta, september18ta, october18ta, november18ta, december18ta, january19ta, february19ta, march19ta, april19ta, may19ta, june19ta, july19ta, august19ta, september19ta, october19ta, november19ta, december19ta, january20ta, february20ta, march20ta) VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24})".format(eid,ta,ta,ta,ta,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta1,ta2,ta2,ta2,ta2,ta2,ta2,ta2,ta2)
        print(sql)
        res = dbconnect(sql)


        tot[0]+=ta
        tot[1]+=ta
        tot[2]+=ta
        tot[3]+=ta
        tot[4]+=ta1
        tot[5]+=ta1
        tot[6]+=ta1
        tot[7]+=ta1
        tot[8]+=ta1
        tot[9]+=ta1
        tot[10]+=ta1
        tot[11]+=ta1
        tot[12]+=ta1
        tot[13]+=ta1
        tot[14]+=ta1
        tot[15]+=ta1
        tot[16]+=ta2
        tot[17]+=ta2
        tot[18]+=ta2
        tot[19]+=ta2
        tot[20]+=ta2
        tot[21]+=ta2
        tot[22]+=ta2
        tot[23]+=ta2

        g18+=4*ta+8*ta1
        g20+=4*ta1+8*ta2 

        sd1=3
        sd2=9
        sd3=15
        sd4=21
        
        sql = "select date1 from dahike"
        res = dbconnect(sql)
        cd1=int(res[0][0])

        sql = "select date2 from dahike"
        res = dbconnect(sql)
        cd2=int(res[0][0])

        sql = "select date3 from dahike"
        res = dbconnect(sql)
        cd3=int(res[0][0])

        sql = "select date4 from dahike"
        res = dbconnect(sql)
        cd4=int(res[0][0])

        cd1=cd1-7 + 3
        cd2=cd2-1 + 9
        cd3=cd3-7 + 15
        cd4=cd4-1 + 21

        # print(cd1,cd2,cd3,cd4)

        da = []
        for i in range(0,3):
            da.append(int(0.12*bp))
        for i in range(3,9):
            da.append(int(0.16*bp1))
        for i in range(9,15):
            da.append(int(0.20*bp1))
        for i in range(15,21):
            da.append(int(0.24*bp2))
        for i in range(21,24):
            da.append(int(0.28*bp2))

        # for i in range(0,24):
        #     print(da[i])


        for i in range(sd1,cd1):
            da[i]=int(0.12*bp)
        da[cd1]=da[cd1]+ (da[cd1]-int(0.12*bp))*(cd1-sd1)
        
        for i in range(sd2,cd2):
            da[i]=int(0.16*bp1)
        da[cd2]=da[cd2]+ (da[cd2]-int(0.16*bp1))*(cd2-sd2)

        for i in range(sd3,cd3):
            da[i]=int(0.20*bp1)
        da[cd3]=da[cd3]+ (da[cd3]-int(0.20*bp1))*(cd3-sd3)

        for i in range(sd4,cd4):
            da[i]=int(0.24*bp2)
        da[cd4]=da[cd4]+ (da[cd4]-int(0.24*bp2))*(cd4-sd4)

        # for i in range(0,24):
        #     print(da[i])

        tot[0]+=da[0]
        tot[1]+=da[1]
        tot[2]+=da[2]
        tot[3]+=da[3]
        tot[4]+=da[4]
        tot[5]+=da[5]
        tot[6]+=da[6]
        tot[7]+=da[7]
        tot[8]+=da[8]
        tot[9]+=da[9]
        tot[10]+=da[10]
        tot[11]+=da[11]
        tot[12]+=da[12]
        tot[13]+=da[13]
        tot[14]+=da[14]
        tot[15]+=da[15]
        tot[16]+=da[16]
        tot[17]+=da[17]
        tot[18]+=da[18]
        tot[19]+=da[19]
        tot[20]+=da[20]
        tot[21]+=da[21]
        tot[22]+=da[22]
        tot[23]+=da[23]

        sql = "insert into da(eid,april18da, may18da, june18da, july18da, august18da, september18da, october18da, november18da, december18da, january19da, february19da, march19da, april19da, may19da, june19da, july19da, august19da, september19da, october19da, november19da, december19da, january20da, february20da, march20da) VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24})".format(eid,da[0],da[1],da[2],da[3],da[4],da[5],da[6],da[7],da[8],da[9],da[10],da[11],da[12],da[13],da[14],da[15],da[16],da[17],da[18],da[19],da[20],da[21],da[22],da[23])
        print(sql)
        res = dbconnect(sql)

        for i in range(0,12):
            g18+=da[i]
        for i in range(12,24):
            g20+=da[i]

        if g18>1000000:
            tds1=int(0.1*g18)
        else:
            tds1=0
        
        if g20>1000000:
            tds2=int(0.1*g20)
        else:
            tds2=0

        tdsr1 = int(tds1/3)
        tdsr2 = int(tds2/3)
        sql = "insert into tds(eid,18to19,19to20,jan19,jan20,feb19,feb20,march19,march20 ) values({0},{1},{2},{3},{4},{5},{6},{7},{8})".format(eid,tds1,tds2,tdsr1,tdsr2,tdsr1,tdsr2,tdsr1,tdsr2)
        print(sql)
        res = dbconnect(sql)

        tot[9]-=tdsr1
        tot[10]-=tdsr1
        tot[11]-=tdsr1
        tot[21]-=tdsr2
        tot[22]-=tdsr2
        tot[23]-=tdsr2

        ttot = 0

        for i in range(0,23):
            ttot+=tot[i]

        sql = "insert into salary(eid,april18sal, may18sal, june18sal, july18sal, august18sal, september18sal, october18sal, november18sal, december18sal, january19sal, february19sal, march19sal, april19sal, may19sal, june19sal, july19sal, august19sal, september19sal, october19sal, november19sal, december19sal, january20sal, february20sal, march20sal,totalsalary) VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25})".format(eid,tot[0],tot[1],tot[2],tot[3],tot[4],tot[5],tot[6],tot[7],tot[8],tot[9],tot[10],tot[11],tot[12],tot[13],tot[14],tot[15],tot[16],tot[17],tot[18],tot[19],tot[20],tot[21],tot[22],tot[23],ttot)
        print(sql)
        res = dbconnect(sql)
        
        return render_template('index.html')
    

@app.route('/dahike',methods = ['POST', 'GET'])
def dahike():
    if request.method == 'POST':
        res = request.form
        print(res)
        date1 = res['date1']
        date1 = date1.split('-')[1]
        date2 = res['date2']
        date2 = date2.split('-')[1]
        date3 = res['date3']
        date3 = date3.split('-')[1]
        date4 = res['date4']
        date4 = date4.split('-')[1]
        sql = "insert into dahike(date1,date2,date3,date4) values('{0}','{1}','{2}','{3}')".format(date1,date2,date3,date4)
        print(sql)
        res = dbconnect(sql)
        return render_template('index.html')


@app.route('/yearly',methods = ['POST', 'GET'])
def yearly():
    if request.method == 'POST':
        res = request.form
        print(res)
        year = res['year']
        
        sql = "select * from salary"
        print(sql)
        res = dbconnect(sql)
        print(res)
        lenres = len(res)
        if year == '2018-2019':
            return render_template('yearly.html',year=1,lenres=lenres,res=res)        
        else:
            return render_template('yearly.html',year=2,lenres=lenres,res=res)
    return render_template('yearly.html',year=1,lenres=0)

@app.route('/monthly',methods = ['POST', 'GET'])
def monthly():
    fda = []
    fhra = []
    fbasic = []
    fname = []
    fta = []
    ftds = []
    flfee = []
    ftot = []
    eid = []
    month = 'month'
    year = 'year'
    if request.method == 'POST':
        res = request.form
        print(res)
        month = res['month']
        year = res['year']
        if year == '2018':
            year = '18'
        if year == '2019':
            year = '19'
        if year == '2020':
            year = '20'   

        sql = "select eid from basicpay"
        print(sql)
        res = dbconnect(sql)
        print(res)
        eid = res
        print(eid)
        for i in range(len(eid)):
            qbasic = month+year+'bp'
            sql = "select {0} from basicpay where eid = {1}".format(qbasic,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            basic = res[0][0]
            print(basic)
            fbasic.append(basic)

            name = 'ename'
            sql = "select {0} from basicpay where eid = {1}".format(name,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            name = res[0][0]
            print(name)
            fname.append(name)

            hra = month+year+'hra'
            sql = "select {0} from hra where eid = {1}".format(hra,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            hra = res[0][0]
            print(hra)
            fhra.append(hra)

            da = month+year+'da'
            sql = "select {0} from da where eid = {1}".format(da,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            da = res[0][0]
            print(da)
            fda.append(da)

            ta = month+year+'ta'
            sql = "select {0} from ta where eid = {1}".format(ta,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            ta = res[0][0]
            print(ta)
            fta.append(ta)

            tds = month+year
            try:
                sql = "select {0} from tds where eid = {1}".format(tds,eid[i][0])
                print(sql)
                res = dbconnect(sql)
                tds = res[0][0]
                print(tds)
            except:
                tds = 0
            ftds.append(tds)

            lfee = 'licencefee'
            sql = "select {0} from quarters where eid = {1}".format(lfee,eid[i][0])
            print(sql)
            res = dbconnect(sql)
            lfee = res[0][0]
            print(lfee)
            flfee.append(lfee)


            tot = lfee+da+ta+hra+basic+tds
            ftot.append(tot)

            print(tot)    

    return render_template('monthly.html',fbasic=fbasic,fhra=fhra,fda=fda,flfee=flfee,fta=fta,eid=eid,ftds=ftds,fname=fname,ftot=ftot,month=month,year=year,leneid = len(eid))

@app.route('/card',methods = ['POST', 'GET'])
def card():
    da = ''
    hra = ''
    basic = ''
    name = ''
    ta = ''
    tds = ''
    lfee = ''
    tot = ''
    eid = ''
    if request.method == 'POST':
        res = request.form
        print(res)
        eid = res['name']
        month = res['month']
        year = res['year']
        if year == '2018':
            year = '18'
        if year == '2019':
            year = '19'
        if year == '2020':
            year = '20'
        qbasic = month+year+'bp'
        sql = "select {0} from basicpay where eid = {1}".format(qbasic,eid)
        print(sql)
        res = dbconnect(sql)
        basic = res[0][0]
        print(basic)

        name = 'ename'
        sql = "select {0} from basicpay where eid = {1}".format(name,eid)
        print(sql)
        res = dbconnect(sql)
        name = res[0][0]
        print(name)

        hra = month+year+'hra'
        sql = "select {0} from hra where eid = {1}".format(hra,eid)
        print(sql)
        res = dbconnect(sql)
        hra = res[0][0]
        print(hra)

        da = month+year+'da'
        sql = "select {0} from da where eid = {1}".format(da,eid)
        print(sql)
        res = dbconnect(sql)
        da = res[0][0]
        print(da)

        ta = month+year+'ta'
        sql = "select {0} from ta where eid = {1}".format(ta,eid)
        print(sql)
        res = dbconnect(sql)
        ta = res[0][0]
        print(ta)

        tds = month+year
        try:
            sql = "select {0} from tds where eid = {1}".format(tds,eid)
            print(sql)
            res = dbconnect(sql)
            tds = res[0][0]
            print(tds)
        except:
            tds = 0

        lfee = 'licencefee'
        sql = "select {0} from quarters where eid = {1}".format(lfee,eid)
        print(sql)
        res = dbconnect(sql)
        lfee = res[0][0]
        print(lfee)



        tot = lfee+da+ta+hra+basic+tds
        print(tot)

    return render_template('card.html',basic=basic,hra=hra,da=da,lfee=lfee,ta=ta,eid=eid,tds=tds,name=name,tot=tot)



if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)