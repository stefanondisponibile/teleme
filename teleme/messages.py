"""
Download messages and stuff.
"""
import argparse
import csv
import datetime
import json
import os
import uuid

from telethon import TelegramClient, sync, types
from tqdm import tqdm

from . import utils

def dump_msg_data(fpath, header, data):
    """Dumps message data to a csv file."""
    with open(fpath, "w") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in tqdm(data, total=len(data), unit="rows", leave=False):
            writer.writerow(row)
    print(f"{len(data)} message{'s' if len(data) > 1 else ''} retrieved.")
    print(f"Dumped dataset @ {fpath}")
    print("Bye! 🐙🐙🐙")

def get_messages(name: str = "B-ubusetette 🍒", limit=None, user=None, dump=True):
    """
    Gets messages from your conversation.

    Args:
    =====
        name (str): target conversation's name;
        limit (int): limit the number of messages retrieved;
        user (str): target username to filter messages from;
        dump (bool): wether to dump the downloaded data or not.

    Returns:
    ========
        msg_data (list) 
    """
    secrets = utils.get_secrets()
    client = TelegramClient("get_messages", secrets.id, secrets.hash)
    csv_header = ("date", "message",)
    msg_data = list()
    with client:
        messages = client.iter_messages(
            name,
            limit=limit,
            from_user=user or client.get_me(),
            filter=types.InputMessagesFilterEmpty,
        )
        for msg in tqdm(messages, unit="messages", leave=False):
            if msg.message and not msg.entities and msg.media is None:
                msg_data.append({
                    csv_header[0]: msg.date,
                    csv_header[1]: msg.message
                })
    curdate = datetime.datetime.now()
    fname = f"{curdate.strftime('%Y%m%d')}_{name.strip().replace(' ', '').title()}_{curdate.strftime('u%S')}.csv"
    datasets_dir = os.path.join(os.path.curdir, "data")
    os.makedirs(datasets_dir, exist_ok=True)
    fpath = os.path.join(datasets_dir, fname)

    if dump == True:
        dump_msg_data(fpath, csv_header, msg_data)
    
    return msg_data
