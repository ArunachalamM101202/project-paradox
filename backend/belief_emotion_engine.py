def adjust_belief_and_emotion(agent, memory_item):
    text = memory_item.text.lower()
    target = memory_item.linked_agent

    if not target or target == agent.name:
        return  # Skip if no clear target

    # Simple rule-based cues for now
    belief_change = 0.0
    emotion_update = {}

    # CONTRADICTION
    if "contradict" in text or "lie" in text:
        belief_change = -2.0
        emotion_update = {"suspicion": 0.3, "anger": 0.2, "stress": 0.1}

    # POSITIVE INTERACTION
    elif "thanked" in text or "helped" in text:
        belief_change = +1.0
        emotion_update = {"joy": 0.2, "satisfaction": 0.2}

    # SUSPICIOUS BEHAVIOR
    elif "sneak" in text or "vault" in text or "spying" in text:
        belief_change = -1.0
        emotion_update = {"suspicion": 0.2, "paranoia": 0.2}

    # Apply updates
    if belief_change != 0.0:
        agent.update_belief(target, belief_change)

    if emotion_update:
        agent.update_emotion(emotion_update)