import webbrowser
import time
    while True:
        print('work!!work!!work!!')
        time.sleep(1800)
        while True:
            print('Break time!!')
            i=input("enter activity 1.music 2.dance 3.cook 4.no-break")
            if i=='music':
                webbrowser.open('https://audiojungle.net/', new=2)
                time.sleep(300)
                break
            if i=='dance':
                webbrowser.open('https://www.steezy.co/', new=2)
                time.sleep(300)
                break
            if i=='cook':
                webbrowser.open('https://www.cookfood.net/', new=2)
                time.sleep(300)
                break
            if i=='nobreak':
                break

