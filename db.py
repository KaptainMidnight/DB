import mysql.connector
from time import time


def get_user_stats(user_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="adminroot",
        database="vkbots"
    )

    crs = mydb.cursor()

    result = crs.execute("SELECT * FROM `accounts` WHERE `uid` = {}".format(user_id))

    row = [result]
    if row["uid"] == user_id:
        return int(row)
    else:
        crs.execute("INSERT INTO `accounts`(`uid`, `money`, `first_message`) VALUES({}, '500', {})".format(user_id, time()))
        result = crs.execute("SELECT * FROM `accounts` WHERE `uid` = {}".format(user_id))
        row = [result]
        mydb.commit()
        return row


get_user_stats(124452681)
