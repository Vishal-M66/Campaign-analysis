from flask import Flask, render_template, request, redirect
import pandas as pd
app = Flask(__name__)
UPLOAD='uploads/data.csv'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f=request.files['file']
    f.save(UPLOAD)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    df=pd.read_csv(UPLOAD)
    ai=df[df['campaign_type']=='AI']
    manual=df[df['campaign_type']=='Manual']
    summary={
      'rows':len(df),
      'ai_open':round(ai['open_rate'].mean(),2),
      'manual_open':round(manual['open_rate'].mean(),2),
      'best_timezone':df.groupby('timezone')['open_rate'].mean().idxmax(),
      'best_hour':int(df.groupby('send_hour')['open_rate'].mean().idxmax())
    }
    return render_template('dashboard.html', s=summary)

if __name__=='__main__':
    app.run(debug=True)
