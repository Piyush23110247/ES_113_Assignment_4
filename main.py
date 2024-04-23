from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Test'
app.config['MYSQL_PASSWORD'] = 'Test'
app.config['MYSQL_DB'] = 'Electoral'
app.config["SECRET_KEY"] = "Abc"

CORS(app)
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question2.html')
def purchaser_bonds():
    cursor = mysql.connection.cursor()
    purchasers = []
    years = []
    try:
        cursor.execute("select DISTINCT NameOfPurchaser from purchase;")
        purchasers = cursor.fetchall()
        cursor.execute("SELECT DISTINCT PurchaseYear FROM Purchase ORDER BY PurchaseYear")
        years = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    purchasers_list = [p[0] for p in purchasers]
    years_list = [y[0] for y in years]

    return render_template('question2.html', purchasers=purchasers_list, years=years_list)


@app.route('/purchaser_bonds_data', methods=['POST'])
def purchaser_bonds_data():
    data = request.json
    purchaser_name = data['purchaser_name']
    purchase_year = data.get('purchase_year')

    cursor = mysql.connection.cursor()
    query = """
    SELECT PurchaseYear AS year, COUNT(*) AS bond_count, SUM(Denominations) AS total_value
    FROM Purchase
    WHERE NameOfPurchaser = %s
    """
    params = [purchaser_name]

    if purchase_year and purchase_year != '':
        query += " AND PurchaseYear = %s"
        params.append(purchase_year)

    query += " GROUP BY PurchaseYear ORDER BY PurchaseYear"

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error fetching data'}), 500
    finally:
        cursor.close()
    
    return jsonify(results)

@app.route('/question3.html')
def get_parties3():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DISTINCT PoliticalPartyName FROM Redeemed")
    parties = cursor.fetchall()
    parties_list = [party[0] for party in parties]

    return render_template('question3.html', parties=parties_list)


@app.route('/party_bonds_data3', methods=['POST'])
def party_bonds_data3():
    data = request.json
    party_name = data['party_name']
    encashment_year = data.get('encashment_year')

    cursor = mysql.connection.cursor()
    query = """
    select count(Denominations),sum(Denominations)/10000000,EncashmentYear from redeemed where PoliticalPartyName = %s group by EncashmentYear ORDER BY EncashmentYear;
    """
    params = [party_name]

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error fetching data'}), 500
    finally:
        cursor.close()
    
    return jsonify(results)


@app.route('/question4.html')
def get_parties4():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DISTINCT PoliticalPartyName FROM Redeemed")
    parties4 = cursor.fetchall()
    parties_list4 = [party[0] for party in parties4]

    return render_template('question4.html', parties=parties_list4)


@app.route('/party_bonds_data4', methods=['POST'])
def party_bonds_data4():
    data = request.json
    party_name = data['party_name']
    encashment_year = data.get('encashment_year')

    cursor = mysql.connection.cursor()
    query = """
    SELECT purchase.NameOfPurchaser, SUM(purchase.Denominations)/10000000 AS total_denominations,count(purchase.Denominations)
FROM purchase
    JOIN redeemed
        ON purchase.BondNumber=redeemed.BondNumber
where redeemed.PoliticalPartyName = %s
GROUP BY  purchase.NameOfPurchaser
order by total_denominations
    """
    params = [party_name]

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error fetching data'}), 500
    finally:
        cursor.close()
    
    return jsonify(results)

@app.route('/question5.html')
def get_parties5():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DISTINCT NameOfPurchaser FROM purchase")
    parties = cursor.fetchall()
    parties_list = [party[0] for party in parties]

    return render_template('question5.html', parties=parties_list)


@app.route('/party_bonds_data5', methods=['POST'])
def party_bonds_data5():
    data = request.json
    party_name = data['party_name']
    encashment_year = data.get('encashment_year')

    cursor = mysql.connection.cursor()
    query = """
    SELECT  redeemed.PoliticalPartyName, SUM(purchase.Denominations)/10000000 AS total_denominations,count(purchase.Denominations)
FROM purchase
    JOIN redeemed
        ON purchase.BondNumber=redeemed.BondNumber
where purchase.NameOfPurchaser = %s
group by redeemed.PoliticalPartyName
order by total_denominations
    """
    params = [party_name]

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error fetching data'}), 500
    finally:
        cursor.close()
    
    return jsonify(results)


@app.route('/question6.html')
def get_parties6():
    return render_template('question6.html')


@app.route('/party_bonds_data6', methods=['POST'])
def party_bonds_data6():
    cursor = mysql.connection.cursor()
    query = """
    SELECT COUNT(Denominations), SUM(Denominations)/10000000 AS BondValue, PoliticalPartyName FROM redeemed GROUP BY PoliticalPartyName order by SUM(Denominations)/10000000 ;
    """
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error fetching data'}), 500
    finally:
        cursor.close()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
