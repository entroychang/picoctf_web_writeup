# Client-side-again - Points: 200

1. First, lets go through the website : https://2019shell1.picoctf.com/problem/37886/
2. Then, we can look up the source code and find out it is similar as "dont-use-client-side - Points: 100"
3. But, it is a little bit tricky cuz it's very "ugly" I mean the source code, so lets beautify it.
    ```
    var _0x5a46 = ['9d025}', '_again_3', 'this', 'Password Verified', 'Incorrect password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
    (function (_0x4bd822, _0x2bd6f7)
    {
        var _0xb4bdb3 = function (_0x1d68f6)
        {
            while (--_0x1d68f6)
            {
                _0x4bd822['push'](_0x4bd822['shift']());
            }
        };
        _0xb4bdb3(++_0x2bd6f7);
    }(_0x5a46, 0x1b3));
    var _0x4b5b = function (_0x2d8f05, _0x4b81bb)
    {
        _0x2d8f05 = _0x2d8f05 - 0x0;
        var _0x4d74cb = _0x5a46[_0x2d8f05];
        return _0x4d74cb;
    };

    function verify()
    {
        checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
        split = 0x4;
        if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3'))
        {
            if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n')
            {
                if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4'))
                {
                    if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT')
                    {
                        if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5'))
                        {
                            if (checkpass['substring'](0x6, 0xb) == 'F{not')
                            {
                                if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6'))
                                {
                                    if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7'))
                                    {
                                        alert(_0x4b5b('0x8'));
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        else
        {
            alert(_0x4b5b('0x9'));
        }
    }
    ```
    As you can see : "'9d025}', '_again_3', 'picoCTF{', 'not_this'"
    And you can easily get the flag.
4. Here is the flag : picoCTF{not_this_again_39d025}

