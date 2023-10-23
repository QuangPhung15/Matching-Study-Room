import googleLogo from '../assets/google.svg';
import facebookLogo from '../assets/facebook.svg';
import './Login.css';

function UserName() {
    return (
        <form>
            <label htmlFor='username'>User Name: </label><br></br>
            <input id="username" type="text"></input>
        </form>
    );
}

function Password() {
    return (
        <form>
            <label htmlFor='password'>Password: </label><br></br>
            <input id="password" type="text"></input>
        </form>
    );
}

function Submit() {
    return (
        <button type="button" disabled>Login</button>
    );
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
            <UserName />
            <Password />
            <Submit />
            <br></br>
            <Google />
            <Facebook />
        </>
        
    );
}

export default Login;