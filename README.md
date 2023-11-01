# TempInbox - Your Temporary Email Solution 📧

Welcome to TempInbox, a Python package designed to simplify your interaction with temporary email addresses. With TempInbox, you can effortlessly generate disposable email addresses and access their content.

## Installation 🛠️

To get started, simply install TempInbox using pip:

```bash
pip install tempinbox
```

## Usage Example 🚀


```python
from tempinbox import TempEmail

# Create a TempEmail instance
client = TempEmail()

# Generate a temporary email address with specific options
email_address = client.generate_temp_email(domain=False, dot_gmail=True, plus_gmail=False)

# Get a list of emails for the generated address
email_list = client.get_mail_list(email_address)

# Get the content of a specific email (ID=2)
email_content = client.get_mail_content(email_address, id=2)

print(email_content)
```

This code snippet demonstrates how to generate a temporary email address with the following options:

- `domain`: Generates an email address without an additional domain.( example@exampledomain.com )
- `dot_gmail`: Generates an email address with a dot and 'gmail.com' (as in the example). ( ex.ex.ex@gmail.com)
- `plus_gmail`: Generates an email address without a plus sign followed by 'gmail.com'. ( example+exam@gmail.com)


## Sample Output 📋

**Generated Email Address**:
```plaintext
m.ar.io.sgl.ade@gmail.com
```

**List of Received Emails**:
```python
{
    'messageData': [
        {
            'messageID': 'ADSVPN',
            'from': 'AI TOOLS',
            'subject': 'Unleash the power of AI with our ultimate directory of online tools!',
            'time': 'Just Now'
        },
        {
            'messageID': 'MThiODcwYWI5Mzk3MDYwNg==',
            'from': 'GPTDOS Access <hi@gptdos.com>',
            'subject': 'GPTDOS Access Code',
            'time': '14 hrs ago'
        },
        {
            'messageID': 'MThiODZmNjlhNzhjYmI5Zg==',
            'from': 'LOVO <hello@lovo.ai>',
            'subject': 'LOVO Newsletter 👻',
            'time': '19 hrs ago'
        }
    ]
}
```

**Email Content (ID=2)**:
```html
<div id="subject-header">
    <b>From: </b>GPTDOS Access &lt;hi@gptdos.com&gt;<br/>
    <b>Subject: </b>GPTDOS Access Code
</div>
<html>
    <head>
        <title></title>
    </head>
    <body>
        您好,<br>
        您在使用 GPTDOS, 请输入验证码:<br/>
        <br/>
        <b>81269658</b>
        <br/>
        GPTDOS<br/>
        <img src="https://u13032898.ct.sendgrid.net/wf/open?upn=rqJJO9-2BJL8i62yHtdgY1cWouC7RdXlcfG3E73dU1e9bPvX1VDl-2BssK4tZTTDPVKiIzaKX2ZiEbmPYpW1BM32GVs-2FvWGiq0R-2BAvavNooikOlxpsMBCJehGSg33aHAZgfSpipfZ1gyuFsxIrfleaNTIuL8Nhu2y5on3fe6rpukhEi-2BHtezMLmZig6IHrWHV12TR94QgEhzPmLoXOHUXx76bqlGEZLGixTo6lCYGECJfgezt6vsLL78PtVSJpanSdYvdoPj-2BNgztK6xsXmw6ZhVWEBeMYBIBQ9BCW7od6JzUo6DaVoLj1iOQcexl-2BOC9COGhif32U42TOV04TnEnFNQ106dIjBtPU3VgTxEZA0cAR35d5AJUgCGRi4-2B-2FqqnPM2-2F" alt="" width="1" height="1" border="0" style="height:1px !important;width:1px !important;border-width:0 !important;margin-top:0 !important;margin-bottom:0 !important;margin-right:0 !important;margin-left:0 !important;padding-top:0 !important;padding-bottom0 !important;padding-right:0 !important;padding-left:0 !important;"/>
    </body>
</html>
```

## Features 🌟

- Quickly generate temporary email addresses.
- Retrieve a list of received emails with details.
- Access the content of specific emails.

## Contribution 🤝

We welcome contributions! If you'd like to enhance TempInbox, feel free to open an issue or create a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

[![GitHub](https://img.shields.io/github/license/ishanoshada/tempinbox)](https://github.com/ishanoshada/tempinbox)
[![GitHub stars](https://img.shields.io/github/stars/ishanoshada/tempinbox)](https://github.com/ishanoshada/tempinbox/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ishanoshada/tempinbox)](https://github.com/ishanoshada/tempinbox/network)

For more information, visit our [GitHub repository](https://github.com/ishanoshada/tempinbox).

**Happy Emailing!** 📬🎉
