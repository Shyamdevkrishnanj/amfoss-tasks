import 'dart:ui';

import 'package:flame/game.dart';
import 'package:flame_game/Bunny_player.dart';
import 'directions.dart';

import 'Bunny_world.dart';

class BunnyGame extends FlameGame {
  BunnyPlayer _bunnyPlayer = BunnyPlayer();
  BunnyWorld _bunnyWorld = BunnyWorld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_bunnyWorld);
    await add(_bunnyPlayer);
    _bunnyPlayer.position = Vector2(400, 920);
    camera.followComponent(_bunnyPlayer,
        worldBounds:
            Rect.fromLTRB(0, 0, _bunnyWorld.size.x, _bunnyWorld.size.y));
  }

  onArrowKeyChanged(Direction direction) {
    _bunnyPlayer.direction = direction;
  }
}
