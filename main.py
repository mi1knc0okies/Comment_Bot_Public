from time import sleep
from datetime import datetime
import praw
import random
import os


# Login info please enter your client ID, Client Secret obtained here https://old.reddit.com/prefs/apps/
# You will also need to enter your username and password. User_agent is the name you want to the bot to display
bot = praw.Reddit(user_agent="Naughty Marie", client_id="I0i4OOSupvEkpg", client_secret="G6fQ8ss9rTz6fIf3UlCFDKpo8_0",
                  username="naughtymarie", password="chester1985")
bot.validate_on_submit = True


# Enter your comment phrases here surrounded by parentheses, separated by a comma ie, "wow", "that's awesome!"
phrases = ['damn that is hot!', 'sexy!', 'mmm yummy!', '🥵🥵🥵', 'if only I had one of these 🍆', 'can I join you?',
           'damn 💦💦💦', '😻😻😻', '💦💦💦', '😍😍😍😍', ]
tp = len(phrases) - 1

# Enter subreddit names with the next number followed by a colon and contained in apostrophes
subs = {1: 'fitgirls', 2: 'BreedingMaterial', 3: 'Nsfw_Amateurs', 4: 'TheThiccness', 5: 'SlimThick', 6: 'curvy',
        7: 'assinthong', 8: 'AmazingCurves', 9: 'whooties', 10: 'booty_queens', 11: 'thickwhitegirls', 12: 'RateMyAss',
        13: 'knockmeup', 14: 'naturaltitties', 15: 'DadWouldBeProud', 16: 'BonerMaterial', 17: 'TotalBabes', 18: 'nsfw2',
        19: 'DirtyConfession', 20: 'interracialwild', 21: 'TexasCuckoldCommunity', 22: 'HotwivesCuckold',
        23: 'happycuckold', 24: 'Cuckold', 25: 'curvy', 26: 'couplesgonewild', 27: 'BlackIsBetter', 28: 'BBCSluts',
        29: 'SnowBunnys', 30: 'amateurgirlsbigcocks', 31: 'homemadexxx', 32: 'Nsfw_Amateurs', 33: 'slutwife',
        34: 'DadWouldBeProud', 35: 'NaughtyWives', 36: 'HotStuffNSFW', 37: 'AmateurSlutWives', 38: 'homesex',
        39: 'nsfw2', 40: 'SnowBunnys', 41: 'RedGIFsPorn', 42: 'DirtyConfession'}
ts = len(subs) - 1

def sleeptimer(time):
    sleeptime = time / 60
    print('Sleeping for '+str(sleeptime)+' mins.', 'It is currently '+str(datetime.now().strftime('%h:%m')))
    return sleep(time)


def close_file(pid):
    with open("commented_post.txt", "w") as f:
        f.write(str(pid) + "\n")
        f.close()


def comment():
    while True:
        if not os.path.isfile("commented_post.txt"):
            pid = []
        else:
            with open("commented_post.txt", "r") as f:
                pid = f.read().split("\n")
                pid = list(filter(None, pid))

        try:
            posts = bot.subreddit(subs[random.randint(1, ts)]).hot(limit=5)
            for submission in posts:
                if submission not in pid:
                    pid.append(submission)
            post_id = []
            post_id.append(pid[random.randint(0, 5)])
            bot.submission(id=post_id[0]).reply(str(phrases[random.randint(0, tp)]))
            close_file(post_id)
            #sleeptimer(random.randint(300,900))
            sleeptimer(45)

        except Exception as e:
            print(e)
            sleeptimer(60)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    comment()
