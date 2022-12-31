import 'dart:ui';

import 'package:flame/game.dart';
import 'directions.dart';
import 'rabbit_player.dart';
import 'rabbit_world.dart';

class BunnyGame extends FlameGame {
  RabbitPlayer _rabbitPlayer = RabbitPlayer();
  RabbitWorld _rabbitWorld = RabbitWorld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_rabbitWorld);
    await add(_rabbitPlayer);
    _rabbitPlayer.position = Vector2(400, 920);
    camera.followComponent(_rabbitPlayer,
        worldBounds:
        Rect.fromLTRB(0, 0, _rabbitWorld.size.x, _rabbitWorld.size.y));
  }

  onArrowKeyChanged(Direction direction) {
    _rabbitPlayer.direction = direction;
  }
}