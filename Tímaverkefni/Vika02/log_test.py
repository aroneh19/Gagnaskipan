from Vika02.logs import Logs

def test_add_log():
    log = Logs()
    time = 2004
    message = "pizza"
    assert log.add_log(time, message)

def test_dates():
    log = Logs()
    start_date = 12
    end_date = 24
    assert log.all_logs(start_date, end_date)

def test_delete_log():
    log = Logs()
    time = 2004
    assert log.delete_log(time)

def test_newest_log():
    log = Logs()
    assert log.newest_log()
