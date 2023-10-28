import googleLogo from '../assets/google.svg';
import facebookLogo from '../assets/facebook.svg';
import './Login.css';
import React, { useState, useEffect } from 'react';
import Home from '../Home/Home.jsx'

function UserName({ value, handleUsernameChange }) {
    return (
        <>
            <label htmlFor='username'>User Name: </label><br></br>
            <input id="username" type="text" placeholder='Your Username' value={value} onChange={handleUsernameChange}></input><br></br>
        </>
    );
}

function Password({ value, handlePasswordChange }) {
    return (
        <>
            <label htmlFor='password'>Password: </label><br></br>
            <input id="password" type="text" placeholder='Your Password' value={value} onChange={handlePasswordChange}></input><br></br>
        </>
    );
}

function Submit({ isDisabled, handleClick }) {
    return (
        <button type="button" disabled={isDisabled} onClick={handleClick}>Login</button>
    );
}

function NormalLogin() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isDisabled, setIsDisabled] = useState(true);

    useEffect(() => {
        handleButtonDisabled();
      }, [username, password]);

    function handleUsernameChange(e) {
        setUsername(e.target.value);
    };

    function handlePasswordChange(e) {
        setPassword(e.target.value);
    };

    function handleButtonDisabled() {
        if (username && password) {
            setIsDisabled(false);
        } else {
            setIsDisabled(true);
        }
    }

    function handleClick() {
        var settings = {
            "url": "http://127.0.0.1:5002/authenticate",
            "method": "POST",
            "timeout": 0,
            "headers": {
              "Content-Type": "application/json"
            },
            "data": JSON.stringify({
              "user_name": username,
              "password": password
            }),
          };
          
          jQuery.ajax(settings).done(function (response) {
            const authen = response['auth'];

            if (authen) {
                return <Home />
            }
          });
    }

    return (
        <form>
            <UserName value={username} handleUsernameChange={handleUsernameChange}/>
            <Password value={password} handlePasswordChange={handlePasswordChange}/>
            <Submit disabled={isDisabled} handleClick={handleClick} />
        </form>
    )
}

function Google() {
    return (
        <button type='button'>
            <img src={googleLogo} alt="Google" className='google'/>
        </button>
    );
}

function Facebook() {
    return (
        <button type='button'>
            <img src={facebookLogo} alt="Facebook" className='facebook'/>
        </button>
    )
}

function Login() {
    return (
        <>
            <NormalLogin />
        </>
        
    );
}

export default Login;