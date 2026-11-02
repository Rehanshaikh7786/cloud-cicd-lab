from app import app

def test_dashboard():
 r=app.test_client().get('/')
 assert r.status_code == 200 and b'CLOUD//NEXUS' in r.data

def test_health():
 r=app.test_client().get('/health')
 assert r.status_code == 200 and r.get_json()['status'] == 'healthy'

def test_ready():
 assert app.test_client().get('/ready').get_json() == {'ready': True}

def test_info():
 r=app.test_client().get('/api/info')
 assert r.status_code == 200 and 'python' in r.get_json()

def test_student():
 assert app.test_client().get('/student').status_code == 200

def test_404():
 r=app.test_client().get('/missing')
 assert r.status_code == 404
