function solution(skill, skillTrees) {
    return skillTrees.reduce((result, skillTree) => {
        let prevSkillIdx = -1
        const isPossibleSkillTree = Array.from(skillTree).every((s) => {
            const skillIdx = skill.indexOf(s)
            if(skillIdx === -1) {
                return true
            }
            if(skillIdx - prevSkillIdx > 1) {
                return false
            } else {
                prevSkillIdx = skillIdx
                return true
            }
        })
        return isPossibleSkillTree ? result + 1 : result
    }, 0)
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))