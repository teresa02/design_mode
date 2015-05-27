# coding=utf-8
from flask import Blueprint, render_template

test_bp = Blueprint('test_bp', __name__)


@test_bp.route('/list', methods=['POST', 'GET'])
def test():
    return render_template('test.html')