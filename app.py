from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/balance')
def balance():
    return render_template('balance.html')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/transaction_history')
def transaction_history():
    return render_template('transaction_history.html')

@app.route('/attendance_history')
def attendance_history():
    return render_template('attendance-history.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/facial_verification')
def facial_verification():
    return render_template('facial-verification.html')

@app.route('/admin_reports')
def admin_reports():
    return render_template('admin-reports.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/recharge')
def recharge():
    return render_template('recharge.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/process_recharge', methods=['POST'])
def process_recharge():
    try:
        recharge_amount = float(request.form.get('recharge_amount'))
        payment_method = request.form.get('payment_method')
        print(f"Recharge Amount: {recharge_amount}, Payment Method: {payment_method}")
        return redirect(url_for('recharge_success'))
    except Exception as e:
        flash(f'Error processing recharge: {e}', 'danger')
    return redirect(url_for('recharge'))


@app.route('/recharge_success')
def recharge_success():
    return render_template('recharge-success.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(debug=True)
