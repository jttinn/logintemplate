# File Name: logintemplate\routes\upload_csv_routes.py
# Version: 1.8
# Last Updated: 17-Feb-2025
# Description: Route for uploading CSV files and inserting data into the stock_lt table.

import os
import csv
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from models import StockLT  # Import the StockLT model
from sqlalchemy.exc import SQLAlchemyError
from . import db

upload_csv_bp = Blueprint('upload_csv', __name__)

# Define the absolute path for the uploads folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@upload_csv_bp.route('/upload_csv', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        if 'csvFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['csvFile']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            print(f"File saved to {filepath}")
            try:
                with open(filepath, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        stock = StockLT()
                        for field in row:
                            if hasattr(stock, field):
                                setattr(stock, field, row[field])
                        db.session.add(stock)
                        print(f"Added stock: {stock}")
                    db.session.commit()
                    print("Database commit successful")
                os.remove(filepath)
                print(f"File {filepath} removed")
                message = f'Successfully uploaded {reader.line_num - 1} records.'
                return render_template('upload_csv.html', message=message)
            except (SQLAlchemyError, Exception) as e:
                db.session.rollback()
                flash(f'Error: {str(e)}')
                print(f"Error: {str(e)}")
                return redirect(request.url)
    return render_template('upload_csv.html')