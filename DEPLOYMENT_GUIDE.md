# 🚀 Deployment Guide - Social Engineering Awareness Program

## 📋 Overview

This guide will help you deploy your Social Engineering Awareness application to the real world using free tier hosting services.

## 🎯 **Recommended: Render (Easiest Free Option)**

### **Step 1: Prepare Your Code**
1. **Create a GitHub repository** and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/social-engineering-awareness.git
   git push -u origin main
   ```

### **Step 2: Deploy to Render**
1. **Sign up** at [render.com](https://render.com)
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `social-engineering-awareness`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### **Step 3: Environment Variables**
Add these in Render dashboard:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### **Step 4: Deploy**
- Click **"Create Web Service"**
- Wait for build to complete
- Your app will be live at: `https://your-app-name.onrender.com`

## 🌐 **Alternative: Railway**

### **Step 1: Deploy to Railway**
1. **Sign up** at [railway.app](https://railway.app)
2. **Click "New Project"** → **"Deploy from GitHub repo"**
3. **Select your repository**
4. **Railway will auto-detect** it's a Python app
5. **Add environment variables** in the dashboard
6. **Deploy automatically**

## 🐘 **Alternative: Heroku**

### **Step 1: Install Heroku CLI**
```bash
# Download from heroku.com/cli
# Or use package manager
```

### **Step 2: Deploy**
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Add environment variables
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key-here

# Deploy
git push heroku main

# Open app
heroku open
```

## 🐍 **Alternative: PythonAnywhere**

### **Step 1: Sign Up**
1. **Create account** at [pythonanywhere.com](https://pythonanywhere.com)
2. **Go to "Web" tab**

### **Step 2: Upload Files**
1. **Upload your project files** via Files tab
2. **Create virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 social-engineering
   pip install -r requirements.txt
   ```

### **Step 3: Configure Web App**
1. **Add new web app** → **Flask** → **Python 3.9**
2. **Set source code** to your project directory
3. **Set WSGI file** to point to your app
4. **Reload** the web app

## 🔧 **Production Configuration**

### **Database Considerations**
For production, consider using:
- **PostgreSQL** (Render, Railway, Heroku provide free tiers)
- **SQLite** (works for small apps, but not recommended for production)

### **Environment Variables**
Set these in your hosting platform:
```
FLASK_ENV=production
SECRET_KEY=your-secure-secret-key
DATABASE_URL=your-database-url
```

### **Security Considerations**
1. **Change default admin password**
2. **Use strong SECRET_KEY**
3. **Enable HTTPS** (most platforms do this automatically)
4. **Set up proper logging**

## 📊 **Monitoring & Analytics**

### **Free Analytics Tools**
- **Google Analytics** - Track user behavior
- **Google Search Console** - Monitor search performance
- **Uptime Robot** - Monitor site availability

### **Logs**
- **Render**: Built-in logging
- **Railway**: Real-time logs
- **Heroku**: `heroku logs --tail`

## 🚀 **Post-Deployment Checklist**

### **✅ Test Your Deployment**
1. **Register a new account**
2. **Login and access dashboard**
3. **Complete a learning module**
4. **Take an assessment**
5. **Test all features**

### **✅ Security Setup**
1. **Change admin password**
2. **Review user registrations**
3. **Monitor for suspicious activity**
4. **Set up backup procedures**

### **✅ Performance Optimization**
1. **Enable caching** if needed
2. **Optimize images** (already done)
3. **Monitor response times**
4. **Set up CDN** if needed

## 🌍 **Custom Domain (Optional)**

### **Free Domain Options**
- **Freenom** - Free .tk, .ml domains
- **GitHub Pages** - Free subdomain
- **Vercel** - Free custom domains

### **SSL Certificate**
- **Let's Encrypt** - Free SSL certificates
- **Most platforms** provide automatic SSL

## 📈 **Scaling Considerations**

### **When to Upgrade**
- **100+ concurrent users**
- **Database size > 1GB**
- **Need custom domain**
- **Require more resources**

### **Paid Options**
- **Render**: $7/month for more resources
- **Railway**: Pay-as-you-use
- **Heroku**: $7/month for hobby dyno

## 🆘 **Troubleshooting**

### **Common Issues**
1. **Build fails**: Check requirements.txt
2. **App won't start**: Check Procfile
3. **Database errors**: Check DATABASE_URL
4. **Static files not loading**: Check file paths

### **Support Resources**
- **Render**: Excellent documentation
- **Railway**: Active Discord community
- **Heroku**: Extensive guides
- **PythonAnywhere**: Python-specific help

## 🎉 **Success!**

Once deployed, your Social Engineering Awareness program will be:
- ✅ **Accessible worldwide**
- ✅ **Available 24/7**
- ✅ **Scalable as needed**
- ✅ **Professional appearance**
- ✅ **Ready for research data collection**

## 📞 **Need Help?**

- **Render**: Built-in support chat
- **Railway**: Discord community
- **Heroku**: Extensive documentation
- **PythonAnywhere**: Python-specific forums

---

**Your application is now ready for real-world deployment!** 🚀 