"""
01_design_patterns.py
Topic: Design Patterns
Goal: Understand what design patterns are, why they exist, and how to think about them
"""

# ------------------
# What Are Design Patterns
# ------------------

# Design patterns are reusable solutions to common software design problems
# They are not code you copy, but general approaches to structure code

# Problem -> Proven solution -> Adapt to your case


# ------------------
# Why Design Patterns Exist
# ------------------

# 1. Avoid reiventing solutions
#   - Common problems already have well-tested approaches

# 2. Improve code structure
#   - Better organization
#   - Clear separation of concerns

# 3. Scalability
#   - Easier to extend systems without breaking existing code

# 4. Communication
#   - Saying "use a Strategy here" is faster than explaining everything


# ------------------
# Categories of Design Patterns
# ------------------

# 1. Creational Patterns
#   - Deal with object creation
#   - Example problems:
#       "How do I control how objects are created?"

#   Examples:
#   - Singleton
#   - Factory
#   - Builder

# 2. Structural Patterns
#   - Deal with how objects are composed
#   - Example problems:
#       "How do I make different systems work together?"

#   Examples:
#   - Adapter
#   - Facade

# 3. Behavioral Patterns
#   - Deal with communication between objects
#   - Example problems:
#       "How do objects interact cleanly?"

#   Examples:
#   - Strategy
#   - Observer


# ------------------
# Mindset
# ------------------

# Design patterns are NOT rules
# You do NOT start by choosing a pattern

# Wrong mindset
#   "I should use a Factory here"

# Correct mindset
#   "I have this problem -> which pattern solves it?"


# ------------------
# Python-Specific Reality
# ------------------

# Python reduces the need for some patterns because:
# - Functions are first-class
# - Dynamic typing
# - Less boilerplate (code required every time you develop a project)

# Strategy patterns can often be replaced with passing functions
# Understand the pattern -> then adapt it to Python


# ------------------
# When to Use Patterns
# ------------------

# Use patterns when:
# - The problem repeats
# - Code is getting messy
# - You need scalability
# - You want clear architecture


# ------------------
# When NOT To Use Patterns
# ------------------

# Avoid patterns when:
# - The problem is simple
# - You're writing small scripts
# - You're forcing complexity


# ------------------
# Next Steps
# ------------------

# For each pattern:
# - Understand the problem it solves
# - Implement it
# - Break it down step-by-step
# - Know when to use it (and when not to)
