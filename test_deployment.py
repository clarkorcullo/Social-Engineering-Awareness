#!/usr/bin/env python3
"""
Simple test script to verify deployment works correctly
"""

import requests
import time

def test_deployment():
    base_url = "https://social-engineering-awareness.onrender.com"
    
    print("🧪 Testing deployment...")
    
    # Test 1: Main page
    try:
        response = requests.get(base_url, timeout=10)
        print(f"✅ Main page: {response.status_code}")
    except Exception as e:
        print(f"❌ Main page error: {e}")
    
    # Test 2: Health check
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"✅ Health check: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    # Test 3: Test route
    try:
        response = requests.get(f"{base_url}/test", timeout=10)
        print(f"✅ Test route: {response.status_code}")
    except Exception as e:
        print(f"❌ Test route error: {e}")
    
    print("\n🎯 Deployment test complete!")
    print("If all tests show ✅, your site is working correctly!")

if __name__ == "__main__":
    test_deployment() 