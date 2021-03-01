from app import app, db
from flask import render_template, request, redirect, jsonify
from app.models import Product

@app.route('/')
def home():
    return "GO to the /api route to see products"

@app.route('/api')
def api():
    return jsonify([p.to_dict() for p in Product.query.all()])