import io
import os
from flask import Flask, jsonify, request, render_template
from flask import make_response
import pymysql
import json
import server


resMsg = {
    "code": -9999,
    "msg": "empty",
}


def register(petName, petSex, petBirthYear, petBirthMonth, petAdoptYear, petAdoptMonth, petWeight, uid):
    try:
        if petName == "":
            resMsg["code"] = 1
            resMsg["msg"] = "You did not enter a pet's name."
            return resMsg
        if petSex == "":
            resMsg["code"] = 2
            resMsg["msg"] = "You did not enter a pet's sex."
            return resMsg
        sql = "SELECT uid FROM user WHERE uid = '%s'" % (uid)
        server.cur.execute(sql)
        server.db.commit()
        result = server.cur.fetchone()
        if type(result) == type(None):
            resMsg["code"] = 3
            resMsg["msg"] = "User with the requested user ID does not exist."
            return resMsg
        else:
            sql = "INSERT INTO pet VALUES(null, '%s', '%s', %s, %s, %s, %s, %s, null, '%s')" % (
                petName, petSex, petBirthYear, petBirthMonth, petAdoptYear, petAdoptMonth, petWeight, uid)
            server.cur.execute(sql)
            server.db.commit()
            resMsg["code"] = 0
            resMsg["msg"] = "Success!"
        return resMsg
    except pymysql.err.IntegrityError as e:
        code, msg = e.args
        resMsg["code"] = code
        resMsg["msg"] = msg
        return resMsg


def getList(uid):
    try:
        sql = "SELECT * FROM pet WHERE uid = '%s'" % (uid)
        server.cur.execute(sql)
        result = server.cur.fetchall()
        return jsonify(result)
    except pymysql.err.IntegrityError as e:
        code, msg = e.args
        resMsg["code"] = code
        resMsg["msg"] = msg
        return resMsg


def getInfo(petid):
    try:
        sql = "SELECT * FROM pet WHERE petid = '%s'" % (petid)
        server.cur.execute(sql)
        result = server.cur.fetchone()
        return jsonify(result)
    except pymysql.err.IntegrityError as e:
        code, msg = e.args
        resMsg["code"] = code
        resMsg["msg"] = msg
        return resMsg


def modify(petid, petName, petSex, petBirthYear, petBirthMonth, petAdoptYear, petAdoptMonth, petWeight, uid):
    try:
        sql = "UPDATE pet SET petname = '%s', petsex = '%s', petbirthyear = %s, petbirthmonth = %s, petadoptyear = %s, petadoptmonth = %s, petweight = %s WHERE petid = %s and uid = '%s'" % (
            petName, petSex, petBirthYear, petBirthMonth, petAdoptYear, petAdoptMonth, petWeight, petid, uid)
        server.cur.execute(sql)
        server.db.commit()
        resMsg["code"] = 0
        resMsg["msg"] = "Success!"
        return jsonify(resMsg)
    except pymysql.err.IntegrityError as e:
        code, msg = e.args
        resMsg["code"] = code
        resMsg["msg"] = msg
        return resMsg


def uploadImg(petid, img):
    try:
        path = './static/petimg/' + petid + '.' + img.mimetype.split('/')[1]
        img.save(path)
        sql = "UPDATE pet SET petimg = '%s' WHERE petid = %s" % (path, petid)
        server.cur.execute(sql)
        server.db.commit()
        resMsg["code"] = 0
        resMsg["msg"] = "Success!"
        return jsonify(resMsg)
    except pymysql.err.IntegrityError as e:
        code, msg = e.args
        resMsg["code"] = code
        resMsg["msg"] = msg
        return resMsg
