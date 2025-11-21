# Quick GitHub Setup Guide

Since GitHub CLI authentication is having issues, here's the simplest manual approach:

## Method 1: Create Repository Manually (EASIEST - 2 minutes)

1. **Go to:** https://github.com/new

2. **Fill in:**
   - Repository name: `ela-heroes`
   - Description: `Educational game for K-6 students learning ELA concepts`
   - Make it **Public**
   - **DO NOT** check "Initialize with README"

3. **Click "Create repository"**

4. **After creation, GitHub will show you commands. Instead, run these in your terminal:**

```bash
cd "c:/Users/Administrator/Desktop/ELA Heroes"
git remote set-url origin https://github.com/connor1570/ela-heroes.git
git push -u origin main
```

When prompted for credentials:
- **Username:** connor1570
- **Password:** Use a Personal Access Token (see Method 2 if you don't have one)

---

## Method 2: Create Personal Access Token (if needed)

1. Go to: https://github.com/settings/tokens/new
2. Note: `ELA Heroes Upload`
3. Expiration: 30 days
4. Check: `repo` (all repository permissions)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this token as your password when pushing

---

## Method 3: Use GitHub Desktop (Simplest GUI)

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. File → Add Local Repository → Browse to "ELA Heroes" folder
4. Click "Publish repository"
5. Done!

---

**Everything is ready to push - choose whichever method you prefer!**
