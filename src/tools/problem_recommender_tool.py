def recommend_problems(topic: str) -> dict:

    topic = topic.lower()

    if "array" in topic:
        problems = [
            "Two Sum",
            "Best Time To Buy Stock",
            "Contains Duplicate",
            "Maximum Subarray",
            "Move Zeroes"
        ]

    elif "string" in topic:
        problems = [
            "Valid Anagram",
            "Longest Common Prefix",
            "Valid Palindrome",
            "Group Anagrams",
            "Longest Substring Without Repeating Characters"
        ]

    elif "linked" in topic:
        problems = [
            "Reverse Linked List",
            "Middle of Linked List",
            "Merge Two Sorted Lists",
            "Linked List Cycle",
            "Remove Nth Node"
        ]

    else:
        problems = [
            "Two Sum",
            "Valid Anagram",
            "Reverse Linked List"
        ]

    return {
        "recommended_problems": problems
    }