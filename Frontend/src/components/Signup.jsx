import React, { Component } from "react";
import "../styles/Signup.css";

export default class Signup extends Component {
    render() {
        return (
            <div className="signup">
                <div className="logo">
                    <img src="logo192.png" alt="" srcset="" />
                    <div className="text">
                        건강한 견생의 일상
                        <br />
                        <strong>푸푸케어</strong>에서 함께 해주세요
                    </div>
                </div>
                <div className="button kakao-sign">
                    <div className="icon">
                        <img src="icon/kakao.png" alt="" />
                    </div>
                    <div className="text">카카오로 가입하기</div>
                </div>
                <div className="button google-sign">
                    <div className="icon">
                        <img src="icon/google.png" alt="" />
                    </div>
                    <div className="text">Gmail로 가입하기</div>
                </div>
                <div className="signin">
                    이미 가입하셨나요? <a href="">로그인하기</a>
                </div>
            </div>
        );
    }
}
