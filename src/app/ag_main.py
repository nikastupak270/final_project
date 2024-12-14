from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from .main import agency, create_offer, get_offer, update_offer

bp = Blueprint('ag_main', __name__)

@bp.route('/')
def index():
    return render_template('ag_main/index.html', offers=agency.get_offers())

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        error = None

        if not name:
            error = 'Потрібна назва туру.'

        if error is not None:
            flash(error)
        else:
            create_offer(name, price)
            return redirect(url_for('ag_main.index'))

    return render_template('ag_main/create.html')

@bp.route('/<int:offer_id>/update', methods=('GET', 'POST'))
@login_required
def update(offer_id):
    offer = get_offer(offer_id)

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        error = None

        if not name or not price:
            error = 'Name and price are required.'

        if error is not None:
            flash(error)
        else:
            update_offer(offer_id, name, price)
            return redirect(url_for('ag_main.index'))

    return render_template('ag_main/update.html', offer=offer)

@bp.route('/<int:offer_id>/delete', methods=('POST',))
@login_required
def delete(offer_id):
    agency.delete_offer(offer_id)
    return redirect(url_for('ag_main.index'))