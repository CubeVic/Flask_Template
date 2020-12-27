from flask import Blueprint, render_template
from flask import current_app as app

#Blueprint configuration
home_bp = Blueprint('home_bp',
                    __name__,
                    template_folder='templates'
                    # static_folder='static')
)

@home_bp.route('/', methods=['GET'])
def index():
    """ Home page """
    return render_template('index.html')