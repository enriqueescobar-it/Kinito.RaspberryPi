import speedtest
import time
import os
import pygsheets
 
def test(spd):    
    spd.download()
    spd.upload()
    res = spd.results.dict()
    #print(res)
    return res["download"], res["upload"], res["ping"]
 
def main():
    #Initialization
    new_rows_res = []
    new_row_avg = []
    da = 0
    ua = 0
    #constant
    LOOPTIMES = 3
 
    #Need to set proper path to the file
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'client_secret.json')
 
    #Get the google worksheet access now
    print("Connecting to google sheet...")
    gc = pygsheets.authorize(service_file=path)
    #Key of the worksheet from the URL
    wrksheet = gc.open_by_key('Replace this with your worksheet key')
    sheetres = wrksheet.worksheet_by_title('results') #1st Sheet
    sheetavg = wrksheet.worksheet_by_title('avgspeed') #2nd sheet
    print("...Connected to '{}'\n".format(wrksheet.title))
    print("Getting servers info")
    s = speedtest.Speedtest()
    servers = [1825]  # Server Maxis (This is a specific server I used; you can change it or remove it to let the API choose the best server)
    s.get_servers(servers) # If you remove the above line, then remove the same from inside brackets here too
    srv = s.get_best_server()
    srv_sponsor = srv["sponsor"]
    srv_id = srv["id"]
 
    #function to convert bytes to mbps
    mbps = lambda b: b / 1024**2
 
    print("Let's find out the net speeds with server: '{}'\n".format(srv_sponsor))
    for i in range(LOOPTIMES):
        print('Making test #{}'.format(i+1))
        d, u, p = test(s)
        da += d
        ua += u
        dt = time.strftime('%d/%m/%Y')
        tm = time.strftime('%H:%M')
        #Put the results into the table for sheet
        new_rows_res.append([srv_id, srv_sponsor, dt, tm, p, round(mbps(d), 2), round(mbps(u), 2)])
       
    #Append the resutls into the google sheet
    sheetres.append_table(new_rows_res)
    #Get average of the multiple readings above
    davg = da / LOOPTIMES
    uavg = ua / LOOPTIMES
    #Append the Avg reading into the 2nd google sheet
    new_row_avg.append([dt, tm, round(mbps(davg), 2), round(mbps(uavg), 2)])
    sheetavg.append_table(new_row_avg)
    print("Done. Results written to google sheets")
 
if __name__ == '__main__':
    main()
