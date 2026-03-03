"""
Task-03: Password Complexity Checker
A tool that assesses password strength based on multiple criteria.
"""

import re
import string


def check_password_strength(password):
    """
    Analyzes password and returns strength score and feedback.
    
    Args:
        password (str): The password to check
    
    Returns:
        dict: Contains score, strength level, and detailed feedback
    """
    score = 0
    feedback = []
    
    # Criteria checks
    length = len(password)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    # Length scoring
    if length >= 8:
        score += 1
        feedback.append("✓ Length is adequate (8+ characters)")
    else:
        feedback.append(f"✗ Too short ({length} chars). Minimum 8 characters recommended")
    
    if length >= 12:
        score += 1
        feedback.append("✓ Good length (12+ characters)")
    
    if length >= 16:
        score += 1
        feedback.append("✓ Excellent length (16+ characters)")
    
    # Character variety scoring
    if has_lower:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    if has_upper:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    if has_digit:
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    if has_special:
        score += 2
        feedback.append("✓ Contains special characters (!@#$%^&* etc.)")
    else:
        feedback.append("✗ Missing special characters")
    
    # Common pattern checks (deduct points)
    common_patterns = [
        r'(123|abc|qwerty|password|admin|letmein)',
        r'(.)\1{2,}',  # Repeated characters (aaa, 111)
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            score -= 1
            feedback.append("⚠ Contains common/predictable pattern")
            break
    
    # Sequential characters check
    if has_sequential_chars(password):
        score -= 1
        feedback.append("⚠ Contains sequential characters (abc, 123)")
    
    # Determine strength level
    if score <= 2:
        strength = "WEAK"
        color = "🔴"
    elif score <= 5:
        strength = "MODERATE"
        color = "🟡"
    elif score <= 7:
        strength = "STRONG"
        color = "🟢"
    else:
        strength = "VERY STRONG"
        color = "🟢🟢"
    
    return {
        'score': max(0, score),
        'max_score': 9,
        'strength': strength,
        'color': color,
        'feedback': feedback
    }


def has_sequential_chars(password):
    """
    Checks if password contains sequential characters.
    
    Args:
        password (str): Password to check
    
    Returns:
        bool: True if sequential characters found
    """
    password_lower = password.lower()
    
    # Check for 3+ sequential letters or numbers
    for i in range(len(password_lower) - 2):
        if password_lower[i:i+3].isalpha():
            if ord(password_lower[i+1]) == ord(password_lower[i]) + 1 and \
               ord(password_lower[i+2]) == ord(password_lower[i+1]) + 1:
                return True
        
        if password_lower[i:i+3].isdigit():
            if int(password_lower[i+1]) == int(password_lower[i]) + 1 and \
               int(password_lower[i+2]) == int(password_lower[i+1]) + 1:
                return True
    
    return False


def generate_password_tips():
    """Returns tips for creating strong passwords."""
    tips = """
    PASSWORD CREATION TIPS:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    1. Use at least 12-16 characters
    2. Mix uppercase and lowercase letters
    3. Include numbers and special characters
    4. Avoid common words and patterns
    5. Don't use personal information (birthdate, name)
    6. Don't reuse passwords across sites
    7. Consider using a passphrase (e.g., "Coffee!Morning@2024")
    8. Use a password manager for complex passwords
    """
    return tips


def main():
    """Main function to run the Password Complexity Checker."""
    print("="*60)
    print("PASSWORD COMPLEXITY CHECKER")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. View password tips")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            password = input("\nEnter password to check: ")
            
            if not password:
                print("\n✗ Password cannot be empty!")
                continue
            
            result = check_password_strength(password)
            
            print("\n" + "="*60)
            print(f"PASSWORD STRENGTH ASSESSMENT")
            print("="*60)
            print(f"Password: {'*' * len(password)}")
            print(f"Length: {len(password)} characters")
            print(f"\nStrength: {result['color']} {result['strength']}")
            print(f"Score: {result['score']}/{result['max_score']}")
            
            print("\n--- Detailed Analysis ---")
            for item in result['feedback']:
                print(f"  {item}")
            
            # Recommendations
            print("\n--- Recommendations ---")
            if result['score'] < 6:
                print("  • Increase password length")
                print("  • Add more character variety")
                print("  • Avoid common patterns")
            elif result['score'] < 8:
                print("  • Consider adding more length or complexity")
            else:
                print("  • Excellent password! Keep it safe and don't reuse it.")
            
            print("="*60)
            
        elif choice == '2':
            print(generate_password_tips())
            
        elif choice == '3':
            print("\nThank you for using Password Complexity Checker!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1-3.")


if __name__ == "__main__":
    main()
