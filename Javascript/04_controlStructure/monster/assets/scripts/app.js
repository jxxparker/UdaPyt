const ATTACK_VALUE = 10;

let chosenJihunLife = 100;
let currentMonsterHealth = chosenJihunLife;
let currentPlayerHealth = chosenJihunLife;

adjustHealthBars(chosenJihunLife);

function attackHandler() {
    const damage = dealMonsterDamage(ATTACK_VALUE);
    currentMonsterHealth -= damage;
}

attackBtn.addEventListener('click', attackHandler);