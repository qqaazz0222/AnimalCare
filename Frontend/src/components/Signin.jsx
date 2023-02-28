import React, { Component } from "react";
import "../styles/Signin.css";

export default class Signin extends Component {
    render() {
        return (
            <div className="signin">
                <div className="logo">
                    <img src="logo192.png" alt="" srcset="" />
                    <div className="text">
                        건강한 견생의 일상
                        <br />
                        <strong>푸푸케어</strong>에서 함께 해주세요
                    </div>
                </div>
                <div className="signindata">
                    <form action="" method="post">
                        <input type="text" placeholder="아이디 입력하기" />
                        <input
                            type="password"
                            placeholder="비밀번호 입력하기"
                        />
                        <button type="submit">로그인</button>
                    </form>
                </div>
                <div className="signin">
                    이미 가입하셨나요? <a href="">로그인하기</a>
                </div>
            </div>
        );
    }
}
