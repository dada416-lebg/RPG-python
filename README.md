 # 🛡️ Python RPG 🗡️



Voici la première version fonctionnelle de mon jeu RPG textuel en Python, que j'ai appelé <strong><em>Python RPG</em></strong>.
<br>
<br>
<div style="text-align: justify">
Dans ce jeu, vous incarnerez un héros qui doit vaincre le Roi Démon pour ramener la paix dans son monde.
</div>
<br>
<div style="text-align: justify">
Pour cela, vous devrez vous entraîner et monter de niveau pour améliorer vos statistiques. Vous affronterez différents ennemis (les sbires du Roi Démon), gagnerez de l'expérience, des potions et de l'argent après les avoir vaincus. Cet argent pourra ensuite être utilisé dans le magasin pour acheter des potions qui vous aideront dans votre aventure.
</div>
<br>
<div style="text-align: justify">
Faites attention à vos risques lors des entraînements ou des combats contre les boss, car si vous perdez tous vos points de vie, vous perdrez toutes vos potions et une partie de votre argent.
</div>
<br>

Le jeu est divisé en six sections principales :

- [Voyage du Héros V1.0](#voyage-du-héros-v10)
  - [Début du Jeu](#début-du-jeu)
  - [Le Village](#le-village)
  - [Terrain d'Entraînement](#terrain-dentraînement)
  - [Magasin](#magasin)
  - [Vérifier les Statistiques](#vérifier-les-statistiques)
  - [Combattre les Boss](#combattre-les-boss)
  - [Installation du Jeu](#installation-du-jeu)
  - [Remarques Finales](#remarques-finales)

<hr>

## Début du Jeu

<hr>

Au début du jeu, vous serez invité à choisir un nom, et vous recevrez 10 points de statistiques à répartir entre quatre attributs :

- **Attaque** : Détermine les dégâts infligés par le joueur.
- **Défense** : Détermine les dégâts ignorés par le joueur.
- **Vitesse** : Détermine les chances d'esquiver une attaque ennemie.
- **Chance de Critique** : Détermine les chances d'infliger un coup critique lors d'une attaque.

Une fois ces points répartis, le jeu vous conduira au [Village](#le-village).

<hr>

## Le Village

<hr>

Le Village agit comme le menu principal du jeu. Vous pouvez y choisir votre prochaine action.

À chaque retour au Village, vos points de vie seront entièrement restaurés. Si vous perdez contre un ennemi, vous serez automatiquement renvoyé ici.

<figure align="center">
<img src="https://i.imgur.com/k2VnjPs.jpg" alt="Menu du Jeu" title="Menu du Jeu">
<figcaption align="center"><em style="font-size: small">Menu du Jeu</em></figcaption>
</figure>

<hr>

## Terrain d'Entraînement

<hr>

C'est ici que vous affronterez les sbires du Roi Démon, accumulerez de l'expérience, des potions et de l'argent.

Les combats sont au tour par tour. Vous pouvez choisir entre utiliser une potion pour récupérer de la vie ou attaquer l'ennemi.

Lorsque vous attaquez, c'est ensuite au tour de l'ennemi de vous attaquer. L'utilisation de potions pendant le combat ne consomme pas de tour.

<figure align="center">
<img src="https://i.imgur.com/h5O0JYV.gif" alt="Combat contre un sbire" title="Combat contre un sbire">
<figcaption align="center"><em style="font-size: small">Exemple de Combat</em></figcaption>
</figure>
<br>
<br>

Une fois l'ennemi vaincu, vous aurez le choix de continuer l'entraînement (pour initier un autre combat) ou de retourner au village pour restaurer vos points de vie.

<hr>

## Magasin

<hr>

Vous pouvez dépenser l'argent gagné en tuant des ennemis pour acheter des potions.

Les potions sont utiles si vous voulez prolonger votre entraînement ou si vous vous apprêtez à affronter un boss.

Chaque potion restaure 20 % de vos points de vie maximum, et vous pouvez transporter un maximum de 10 potions à la fois.

<figure align="center">
<img src="https://i.imgur.com/59DnsM4.jpg" alt="Magasin" title="Magasin">
<figcaption align="center"><em style="font-size: small">Magasin</em></figcaption>
</figure>

<hr>

## Vérifier les Statistiques

<hr>

Au fil du jeu, vous accumulerez des points de statistiques à dépenser pour améliorer vos attributs. Cette section vous permet de les répartir entre les 4 attributs mentionnés dans la section [Début du Jeu](#début-du-jeu) et de consulter vos statistiques actuelles.

<figure align="center">
<img src="https://i.imgur.com/gRkZHDc.jpg" alt="Statistiques du joueur" title="Statistiques du joueur">
<figcaption align="center"><em style="font-size: small">Statistiques du joueur</em></figcaption>
</figure>
<br>
<br>

Chaque attribut atteint son niveau maximum à 10.

<figure align="center">
<img src="https://i.imgur.com/yqlwbTj.jpg" alt="Dépense des points" title="Dépense des points">
<figcaption align="center"><em style="font-size: small">Dépense des points</em></figcaption>
</figure>

<hr>

## Combattre les Boss

<hr>

Le jeu contient quatre boss :

- **Abadon**
- **Mammon**
- **Belphégor**
- **Lucifer** (le Roi Démon)

Les mécaniques de combat contre les boss sont les mêmes que contre les sbires, mais les boss sont beaucoup plus puissants. Si vous n'êtes pas suffisamment entraîné, il sera presque impossible de les vaincre.

<figure align="center">
<img src="https://i.imgur.com/xiVDp1T.jpg" alt="Combat contre un boss sans entraînement" title="Combat contre un boss sans entraînement">
<figcaption align="center"><em style="font-size: small">Combat sans entraînement</em></figcaption>
</figure>

<hr>
