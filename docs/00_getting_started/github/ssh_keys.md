# SSH-ключі для GitHub — Windows, macOS і Linux

SSH-ключ дозволяє працювати з GitHub (`clone`, `pull`, `push`) без введення логіна й пароля під час кожної операції.

Ключ потрібно створити **один раз на кожному комп'ютері**, з якого ти працюєш з GitHub.

> **Важливо:** команди залежать від операційної системи й термінала.  
> `Get-Content` і `Set-Clipboard` — це команди **Windows PowerShell**. Вони не працюють у `zsh` або `bash` на macOS/Linux.

---

## 1. Визнач свою систему

У цьому розділі використовуються такі термінали:

| Система | Термінал / shell | Команди нижче |
|---|---|---|
| Windows 10/11 | PowerShell | `powershell` |
| macOS | Terminal, `zsh` | `bash` |
| Linux | Terminal, `bash` або `zsh` | `bash` |

У **PyCharm Terminal** використовуй команди для тієї системи й shell, які реально відкриті в терміналі.

Наприклад, якщо бачиш:

```text
zsh: command not found: Get-Content
zsh: command not found: Set-Clipboard
```

це означає, що ти запустив PowerShell-команду в `zsh`. Для macOS/Linux потрібно використовувати команди з відповідного розділу нижче.

---

## 2. Перевір, чи SSH-ключ уже існує

### Windows — PowerShell

```powershell
Get-ChildItem "$env:USERPROFILE\.ssh" -Filter *.pub
```

### macOS / Linux

```bash
find ~/.ssh -maxdepth 1 -type f -name "*.pub" -print 2>/dev/null
```

Якщо бачиш файл на кшталт:

```text
id_ed25519.pub
```

то публічний ключ уже існує. **Не створюй новий ключ без потреби.** Перейди до кроку 4 — копіювання публічного ключа.

Якщо нічого не знайдено — створи новий ключ.

---

## 3. Створи новий SSH-ключ

Команда однакова для Windows, macOS і Linux:

```bash
ssh-keygen -t ed25519 -C "твій_email_на_GitHub"
```

Заміни `твій_email_на_GitHub` на email, який використовуєш у GitHub, наприклад:

```bash
ssh-keygen -t ed25519 -C "student@example.com"
```

Після запуску з'явиться запит приблизно такого вигляду:

```text
Enter file in which to save the key (.../.ssh/id_ed25519):
```

Натисни **Enter**, щоб використати стандартний шлях.

Далі:

```text
Enter passphrase (empty for no passphrase):
```

Можна:

- ввести пароль для SSH-ключа — це безпечніший варіант;
- або натиснути **Enter** двічі, щоб залишити ключ без пароля.

> Якщо система запитує, чи **перезаписати (`overwrite`) існуючий `id_ed25519`**, не погоджуйся автоматично. Старий ключ може вже використовуватися для GitHub або інших серверів.

Після створення будуть два файли:

```text
id_ed25519
id_ed25519.pub
```

- `id_ed25519` — **приватний ключ**;
- `id_ed25519.pub` — **публічний ключ**.

⚠️ **Приватний ключ `id_ed25519` нікому не надсилай і нікуди не публікуй.**  
Для GitHub потрібен тільки файл із `.pub`.

---

## 4. Скопіюй публічний ключ

### Windows — PowerShell

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" | Set-Clipboard
```

Після цього ключ уже знаходиться в буфері обміну.

Якщо хочеш просто побачити його в терміналі:

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
```

### macOS

Скопіювати ключ у буфер обміну:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

Або показати його в терміналі:

```bash
cat ~/.ssh/id_ed25519.pub
```

### Linux

Найбільш універсальний варіант — показати ключ у терміналі:

```bash
cat ~/.ssh/id_ed25519.pub
```

Потім виділи весь рядок і скопіюй його.

Якщо у твоїй системі встановлено `wl-copy` (часто Wayland), можна скопіювати одразу:

```bash
wl-copy < ~/.ssh/id_ed25519.pub
```

Для систем із `xclip`:

```bash
xclip -selection clipboard < ~/.ssh/id_ed25519.pub
```

Публічний ключ виглядає приблизно так:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... student@example.com
```

Копіюй **увесь рядок повністю**.

---

## 5. Додай публічний ключ у GitHub

Відкрий сторінку:

[GitHub → Settings → SSH and GPG keys → New SSH key](https://github.com/settings/ssh/new)

Заповни:

- **Title** — зрозуміла назва комп'ютера, наприклад `Windows-PC`, `MacBook-Air`, `Ubuntu-Laptop`;
- **Key type** — `Authentication Key`;
- **Key** — встав скопійований публічний ключ.

Для вставки:

- Windows/Linux — зазвичай `Ctrl+V`;
- macOS — `Cmd+V`.

Натисни **Add SSH key**.

---

## 6. Перевір підключення до GitHub

Команда однакова для Windows, macOS і Linux:

```bash
ssh -T git@github.com
```

Під час першого підключення може з'явитися запит:

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Введи:

```text
yes
```

Успішна відповідь виглядатиме приблизно так:

```text
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

Це **нормальна відповідь**. Вона означає, що GitHub розпізнав твій SSH-ключ.

Після цього можна повторити потрібну Git-команду:

```bash
git clone ...
git pull
git push
```

---

## 7. Якщо бачиш `Permission denied (publickey)`

Спочатку перевір, чи існує публічний ключ.

### Windows — PowerShell

```powershell
Get-ChildItem "$env:USERPROFILE\.ssh" -Filter *.pub
```

### macOS / Linux

```bash
find ~/.ssh -maxdepth 1 -type f -name "*.pub" -print 2>/dev/null
```

Потім перевір:

1. чи додано саме цей `.pub` ключ у **GitHub → Settings → SSH and GPG keys**;
2. чи команда `ssh -T git@github.com` працює;
3. чи репозиторій використовує SSH-адресу, наприклад:

```text
git@github.com:USERNAME/REPOSITORY.git
```

Перевірити адресу поточного репозиторію:

```bash
git remote -v
```

---

## 8. Якщо в системному терміналі працює, а в PyCharm — ні

Спочатку відкрий **Terminal** усередині PyCharm і виконай:

```bash
ssh -T git@github.com
```

Якщо в системному Terminal/PowerShell команда працює, а в PyCharm — ні, перевір, який shell використовує PyCharm.

У PyCharm:

**Settings / Preferences → Tools → Terminal → Shell path**

Типові значення:

- Windows PowerShell — `powershell.exe` або `pwsh.exe`;
- macOS — `/bin/zsh`;
- Linux — `/bin/bash` або `/bin/zsh`.

Не змішуй команди різних shell. Наприклад:

```powershell
Get-Content ... | Set-Clipboard
```

працює в **PowerShell**, але не працює в `zsh` або `bash`.

---

## Коротка шпаргалка

| Дія | Windows PowerShell | macOS | Linux |
|---|---|---|---|
| Перевірити `.pub` ключ | `Get-ChildItem "$env:USERPROFILE\.ssh" -Filter *.pub` | `find ~/.ssh -maxdepth 1 -type f -name "*.pub" -print 2>/dev/null` | `find ~/.ssh -maxdepth 1 -type f -name "*.pub" -print 2>/dev/null` |
| Створити ключ | `ssh-keygen -t ed25519 -C "email"` | `ssh-keygen -t ed25519 -C "email"` | `ssh-keygen -t ed25519 -C "email"` |
| Скопіювати `.pub` | `Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" \| Set-Clipboard` | `pbcopy < ~/.ssh/id_ed25519.pub` | `cat ~/.ssh/id_ed25519.pub` |
| Перевірити GitHub | `ssh -T git@github.com` | `ssh -T git@github.com` | `ssh -T git@github.com` |

> ⚠️ Надсилати викладачу можна тільки **публічний ключ** (`id_ed25519.pub`).  
> **Приватний ключ** (`id_ed25519`) нікому не передавай.
