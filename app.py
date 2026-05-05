from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'game.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ENDING_RULES = [
    {
        'key': 'anarchy',
        'name': '無政府暴動',
        'condition': '民粹激進 >= 80 且 社會秩序 <= 30',
        'description': '極端民粹摧毀理性討論，社會陷入街頭暴力與政府失能。'
    },
    {
        'key': 'authoritarian',
        'name': '新威權時代',
        'condition': '社會秩序 >= 80 且 自由平權 <= 30',
        'description': '人民為了換取秩序讓渡自由，政府取得過度控制權。'
    },
    {
        'key': 'progressive_utopia',
        'name': '進步烏托邦',
        'condition': '自由平權 >= 70 且 進步主義 >= 70 且 社會秩序 >= 50',
        'description': '自由、包容與制度穩定同時維持，社會進入高度進步狀態。'
    },
    {
        'key': 'populist_regime',
        'name': '極端民粹政權',
        'condition': '民粹激進 >= 70 且 社會秩序 >= 70',
        'description': '以多數暴力之名形成排除異己的政治秩序。'
    },
    {
        'key': 'muddy_democracy',
        'name': '泥淖中的民主',
        'condition': '其他所有數值組合',
        'description': '社會沒有崩潰，但在爭吵、妥協與內耗中繼續前進。'
    }
]

def determine_ending(freedom, order, progress, populism):
    if populism >= 80 and order <= 30:
        return ENDING_RULES[0]
    if order >= 80 and freedom <= 30:
        return ENDING_RULES[1]
    if freedom >= 70 and progress >= 70 and order >= 50:
        return ENDING_RULES[2]
    if populism >= 70 and order >= 70:
        return ENDING_RULES[3]
    return ENDING_RULES[4]

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_playable = db.Column(db.Boolean, default=False)
    image_filename = db.Column(db.String(100), nullable=True)
    relationships_text = db.Column(db.Text, nullable=True)
    stances_text = db.Column(db.Text, nullable=True)
    personal_stats_config = db.Column(db.Text, nullable=True) # JSON string representing starting personal stats

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    x_pos = db.Column(db.Integer, nullable=False)
    y_pos = db.Column(db.Integer, nullable=False)
    
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)
    target_role = db.Column(db.String(50), nullable=True) # If set, only this role sees the event
    is_news = db.Column(db.Boolean, default=False)
    relationship_effects_text = db.Column(db.Text, nullable=True)
    persuasion_config = db.Column(db.Text, nullable=True) # JSON string for persuasion options
    
    option_a_text = db.Column(db.String(100), nullable=False)
    option_a_freedom = db.Column(db.Integer, default=0)
    option_a_order = db.Column(db.Integer, default=0)
    option_a_progress = db.Column(db.Integer, default=0)
    option_a_populism = db.Column(db.Integer, default=0)
    option_a_result_text = db.Column(db.Text, nullable=False)
    option_a_personal_effects = db.Column(db.Text, nullable=True) # JSON string
    option_a_explanation = db.Column(db.Text, nullable=True)
    
    option_b_text = db.Column(db.String(100), nullable=False)
    option_b_freedom = db.Column(db.Integer, default=0)
    option_b_order = db.Column(db.Integer, default=0)
    option_b_progress = db.Column(db.Integer, default=0)
    option_b_populism = db.Column(db.Integer, default=0)
    option_b_result_text = db.Column(db.Text, nullable=False)
    option_b_personal_effects = db.Column(db.Text, nullable=True) # JSON string
    option_b_explanation = db.Column(db.Text, nullable=True)

class PlayerLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    final_freedom = db.Column(db.Integer)
    final_order = db.Column(db.Integer)
    final_progress = db.Column(db.Integer)
    final_populism = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html lang="zh-Hant">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>萬能的鑰匙後端</title>
        <style>
          body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            background: #f4efe3;
            color: #24313d;
            font-family: "Noto Sans TC", "Microsoft JhengHei", system-ui, sans-serif;
          }
          main {
            width: min(720px, calc(100% - 32px));
            background: white;
            border: 1px solid #d9e0e5;
            border-radius: 10px;
            box-shadow: 0 12px 30px rgba(35, 46, 57, 0.08);
            padding: 28px;
          }
          h1 { margin: 0 0 10px; color: #386f8f; }
          p { line-height: 1.7; }
          a {
            display: inline-block;
            margin: 8px 8px 0 0;
            padding: 10px 14px;
            border-radius: 8px;
            background: #386f8f;
            color: white;
            font-weight: 700;
            text-decoration: none;
          }
          code {
            background: #eef3f5;
            border-radius: 6px;
            padding: 2px 6px;
          }
        </style>
      </head>
      <body>
        <main>
          <h1>後端已啟動</h1>
          <p>這個 Render 網址是用來儲存玩家結果與查看管理後台的，不是主要分享給玩家玩的前端網址。</p>
          <p>玩家遊戲頁請使用 GitHub Pages。GitHub Pages 的前端會把資料送回這個後端。</p>
          <a href="/admin">進入後台</a>
          <a href="/api/health">檢查連線</a>
          <a href="/play">本機/備用遊戲頁</a>
          <p>如果免費 Render 服務剛醒來，第一次載入可能會等 30 秒到 1 分鐘；醒來後會比較快。</p>
        </main>
      </body>
    </html>
    '''

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'database': 'connected',
        'characters': Character.query.count(),
        'events': Event.query.count(),
        'logs': PlayerLog.query.count(),
        'time': datetime.utcnow().isoformat()
    })

# API Routes
@app.route('/api/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    import json
    res = []
    for c in characters:
        stats = {}
        if c.personal_stats_config:
            try:
                stats = json.loads(c.personal_stats_config)
            except:
                pass
        res.append({
            'id': c.id, 'name': c.name, 'role': c.role, 
            'description': c.description, 'is_playable': c.is_playable,
            'image_filename': c.image_filename,
            'relationships_text': c.relationships_text,
            'stances_text': c.stances_text,
            'personal_stats': stats
        })
    return jsonify(res)

@app.route('/api/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{
        'id': l.id, 'name': l.name, 'description': l.description,
        'x_pos': l.x_pos, 'y_pos': l.y_pos
    } for l in locations])

@app.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    import json
    res = []
    for e in events:
        eff_a, eff_b = {}, {}
        persuasion = None
        try:
            if e.option_a_personal_effects: eff_a = json.loads(e.option_a_personal_effects)
            if e.option_b_personal_effects: eff_b = json.loads(e.option_b_personal_effects)
            if e.persuasion_config: persuasion = json.loads(e.persuasion_config)
        except:
            pass
            
        res.append({
            'id': e.id, 'title': e.title, 'description': e.description,
            'image_filename': e.image_filename,
            'target_role': e.target_role,
            'is_news': e.is_news,
            'relationship_effects_text': e.relationship_effects_text,
            'persuasion_config': persuasion,
            'options': [
                {
                    'id': 'A', 'text': e.option_a_text, 'result_text': e.option_a_result_text,
                    'explanation': e.option_a_explanation,
                    'effects': {'freedom': e.option_a_freedom, 'order': e.option_a_order, 'progress': e.option_a_progress, 'populism': e.option_a_populism},
                    'personal_effects': eff_a
                },
                {
                    'id': 'B', 'text': e.option_b_text, 'result_text': e.option_b_result_text,
                    'explanation': e.option_b_explanation,
                    'effects': {'freedom': e.option_b_freedom, 'order': e.option_b_order, 'progress': e.option_b_progress, 'populism': e.option_b_populism},
                    'personal_effects': eff_b
                }
            ]
        })
    return jsonify(res)

@app.route('/api/logs', methods=['POST'])
def save_log():
    data = request.json
    new_log = PlayerLog(
        player_name=data['player_name'],
        character_id=data['character_id'],
        final_freedom=data['final_freedom'],
        final_order=data['final_order'],
        final_progress=data['final_progress'],
        final_populism=data['final_populism']
    )
    db.session.add(new_log)
    db.session.commit()
    ending = determine_ending(
        new_log.final_freedom,
        new_log.final_order,
        new_log.final_progress,
        new_log.final_populism
    )
    return jsonify({'status': 'success', 'ending': ending})

@app.route('/api/logs', methods=['GET'])
def get_logs():
    logs = PlayerLog.query.order_by(PlayerLog.created_at.desc()).all()
    character_map = {c.id: c for c in Character.query.all()}
    rows = []
    for l in logs:
        character = character_map.get(l.character_id)
        ending = determine_ending(l.final_freedom, l.final_order, l.final_progress, l.final_populism)
        rows.append({
            'id': l.id,
            'player_name': l.player_name,
            'character_id': l.character_id,
            'character_name': character.name if character else None,
            'character_role': character.role if character else None,
            'final_freedom': l.final_freedom,
            'final_order': l.final_order,
            'final_progress': l.final_progress,
            'final_populism': l.final_populism,
            'ending_key': ending['key'],
            'ending_name': ending['name'],
            'created_at': l.created_at.isoformat()
        })
    return jsonify(rows)

@app.route('/api/admin/overview', methods=['GET'])
def admin_overview():
    import json
    characters = Character.query.order_by(Character.id).all()
    events = Event.query.order_by(Event.id).all()
    logs = PlayerLog.query.order_by(PlayerLog.created_at.desc()).all()

    ending_counts = {rule['key']: {'name': rule['name'], 'count': 0} for rule in ENDING_RULES}
    for log in logs:
        ending = determine_ending(log.final_freedom, log.final_order, log.final_progress, log.final_populism)
        ending_counts[ending['key']]['count'] += 1

    story_events = []
    for event in events:
        persuasion = None
        if event.persuasion_config:
            try:
                persuasion = json.loads(event.persuasion_config)
            except Exception:
                persuasion = None
        story_events.append({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'target_role': event.target_role or '所有玩家',
            'is_news': event.is_news,
            'image_filename': event.image_filename,
            'relationship_effects_text': event.relationship_effects_text,
            'persuasion_config': persuasion,
            'branches': [
                {
                    'id': 'A',
                    'text': event.option_a_text,
                    'result_text': event.option_a_result_text,
                    'explanation': event.option_a_explanation,
                    'effects': {
                        'freedom': event.option_a_freedom,
                        'order': event.option_a_order,
                        'progress': event.option_a_progress,
                        'populism': event.option_a_populism
                    }
                },
                {
                    'id': 'B',
                    'text': event.option_b_text,
                    'result_text': event.option_b_result_text,
                    'explanation': event.option_b_explanation,
                    'effects': {
                        'freedom': event.option_b_freedom,
                        'order': event.option_b_order,
                        'progress': event.option_b_progress,
                        'populism': event.option_b_populism
                    }
                }
            ]
        })

    return jsonify({
        'counts': {
            'characters': len(characters),
            'events': len(events),
            'logs': len(logs)
        },
        'ending_rules': ENDING_RULES,
        'ending_counts': list(ending_counts.values()),
        'characters': [{
            'id': c.id,
            'name': c.name,
            'role': c.role,
            'is_playable': c.is_playable
        } for c in characters],
        'events': story_events
    })

if __name__ == '__main__':
    app.run(debug=True)
